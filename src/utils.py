"""Utility helpers for USB Secure Wipe project."""
import os
import time


SECTOR = 512
DEFAULT_BLOCK = 16 * 1024 * 1024




def human_bytes(n):
for unit in ["B","KiB","MiB","GiB","TiB"]:
if n < 1024 or unit=="TiB":
return f"{n:.2f} {unit}"
n /= 1024




def get_device_size_bytes(path):
try:
if os.name != "nt":
with open(path, "rb", buffering=0) as f:
f.seek(0, os.SEEK_END)
return f.tell()
except Exception:
pass
return None
