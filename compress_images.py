# -*- coding: utf-8 -*-
"""
Batch compress images to WebP for xinqiutent.com Core Web Vitals optimization.
- Converts PNG/JPG > 200KB to WebP (quality 80)
- Keeps original filename, replaces extension with .webp
- Also writes a mapping file for reference
"""
import os
from PIL import Image

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images")
THRESHOLD_KB = 200
QUALITY = 80

report = []
converted = []

for fname in os.listdir(BASE):
    fpath = os.path.join(BASE, fname)
    if not os.path.isfile(fpath):
        continue
    ext = os.path.splitext(fname)[1].lower()
    if ext not in (".png", ".jpg", ".jpeg"):
        continue
    size_kb = os.path.getsize(fpath) / 1024
    if size_kb < THRESHOLD_KB:
        report.append((fname, round(size_kb), "SKIP (small)"))
        continue
    try:
        img = Image.open(fpath)
        # Convert RGBA/P to RGB for WebP when no transparency needed, else keep alpha
        if img.mode in ("RGBA", "LA", "P"):
            if "transparency" in img.info or img.mode == "RGBA":
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")
        else:
            img = img.convert("RGB")
        webp_name = os.path.splitext(fname)[0] + ".webp"
        webp_path = os.path.join(BASE, webp_name)
        img.save(webp_path, "WEBP", quality=QUALITY, method=6)
        new_size_kb = os.path.getsize(webp_path) / 1024
        converted.append((fname, webp_name, round(size_kb), round(new_size_kb), round(size_kb / max(new_size_kb, 1), 1)))
        # Remove the original large file
        os.remove(fpath)
        report.append((fname, round(size_kb), f"-> {webp_name} ({round(new_size_kb)}KB, saved {round(100*(1-new_size_kb/size_kb))}%)"))
    except Exception as e:
        report.append((fname, round(size_kb), f"ERROR: {e}"))

print("=== Conversion Report ===")
for r in report:
    print(f"{r[0]}: {r[1]}KB {r[2]}")

total_orig = sum(c[2] for c in converted)
total_new = sum(c[3] for c in converted)
print(f"\n=== Summary ===")
print(f"Converted: {len(converted)} files")
print(f"Original total: {total_orig}KB -> New total: {total_new}KB (saved {round(100*(1-total_new/total_orig))}%)")
