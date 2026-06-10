import os
import sys

pdf_path = r"I:/xwechat_files/csclovezsy_bfa6/temp/RWTemp/2026-04/027ecbb2036511f33b1c4e4372adbed7/12经典轻量化绿色(2).pdf"
output_dir = "temp_images"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    import pymupdf # fitz
except ImportError:
    print("pymupdf not installed, trying to install...")
    import subprocess
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
        import pymupdf
    except Exception as e:
        print(f"Failed to install pymupdf: {e}")
        sys.exit(1)

try:
    doc = pymupdf.open(pdf_path)
    print(f"Total pages: {len(doc)}")

    for i in range(len(doc)):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        out_path = os.path.join(output_dir, f"page_{i+1}.png")
        pix.save(out_path)
        print(f"Saved: {out_path}")
except Exception as e:
    print(f"Error converting PDF: {e}")
