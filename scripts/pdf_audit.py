#!/usr/bin/env python3
"""Usage: pdf_audit.py report.pdf [extra banned strings...]
Automatic checks: text near page edge, orphan last lines, forbidden strings. (Word-box overlap is NOT checked: Chrome Type3 fonts give bad boxes. Overlaps are found by looking at page images.)"""
import sys, re, subprocess, collections
import xml.etree.ElementTree as ET
pdf = sys.argv[1]
banned = sys.argv[2:]  # extra strings that must count 0
out = subprocess.run(["pdftotext","-bbox-layout",pdf,"-"],capture_output=True,text=True).stdout
out = re.sub(r'<!DOCTYPE[^>]*>','',out); out = re.sub(r'xmlns="[^"]*"','',out)
root = ET.fromstring(out)
issues=0
for pn,page in enumerate(root.iter('page'),1):
    W=float(page.get('width')); H=float(page.get('height'))
    words=[(float(w.get('xMin')),float(w.get('yMin')),float(w.get('xMax')),float(w.get('yMax')),w.text or '') for w in page.iter('word')]
    # 1 out of safe margin (>=12pt)
    for x0,y0,x1,y1,t in words:
        if x0<12 or y0<8 or x1>W-12 or y1>H-4:
            print(f"p{pn}: text near/over edge: {t!r} ({x0:.0f},{y0:.0f},{x1:.0f},{y1:.0f})"); issues+=1
    # 3 orphan lines: a block's last line with <=3 chars
    for blk in page.iter('block'):
        lines=[ ''.join((w.text or '') for w in l.iter('word')) for l in blk.iter('line')]
        if len(lines)>=2 and len(lines[-1])<=3 and not re.fullmatch(r'[\d\W]*',lines[-1]):
            print(f"p{pn}: orphan last line {lines[-1]!r} after {lines[-2][-12:]!r}"); issues+=1
txt=subprocess.run(["pdftotext","-layout",pdf,"-"],capture_output=True,text=True).stdout
for s in ["未取得","…","TODO","XXX","NaN","undefined"]+banned:
    n=txt.count(s)
    if n: print(f"string {s!r}: {n}"); issues+=1
print("pages:",len(list(root.iter('page'))),"issues:",issues)

# pixel check: ink in outer margins / content collision with footer band
try:
    from PIL import Image
    import tempfile, glob, os
    d=tempfile.mkdtemp(); subprocess.run(["pdftoppm","-r","60","-png",pdf,d+"/p"],capture_output=True)
    for f in sorted(glob.glob(d+"/p-*.png")):
        im=Image.open(f).convert("L"); w,h=im.size; px=im.load()
        def ink(x0,y0,x1,y1): return sum(1 for x in range(x0,x1) for y in range(y0,y1) if px[x,y]<200)
        m=int(w*0.012)
        for name,box in {"left":(0,int(h*0.06),m,int(h*0.94)),"right":(w-m,int(h*0.06),w,int(h*0.94)),"bottom":(0,h-int(h*0.006),w,h)}.items():
            if ink(*box)>3: print(os.path.basename(f),"ink in",name,"margin")
except Exception as e: print("pixel check skipped:",e)
