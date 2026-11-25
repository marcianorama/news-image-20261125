"""Entry program for news-image-20261125.
Copies the bundled entry.png to /output/entry.png.
Deterministic, no network, Python stdlib only.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

if not os.path.exists(SRC):
    raise FileNotFoundError("bundled entry.png not found beside main.py")
os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
# The copy is byte-for-byte identical to the bundled image, by design.
print(DST)
