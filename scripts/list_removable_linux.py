#!/usr/bin/env python3
"""
list_removable_linux.py
List removable block devices on Linux with size info and mount status.
Usage: python3 scripts/list_removable_linux.py
"""
import json
import subprocess


def lsblk_json():
out = subprocess.check_output(["lsblk","-J","-o","NAME,TYPE,SIZE,MOUNTPOINT,RM,RO,MODEL,TRAN"]).decode()
return json.loads(out)["blockdevices"]


def flatten(devs, parent=""):
for d in devs:
yield d, parent
if "children" in d and d["children"]:
yield from flatten(d["children"], d["name"])


def main():
devs = lsblk_json()
print(f"{'PATH':<15} {'TYPE':<6} {'RM':<2} {'RO':<2} {'SIZE':>8} {'MOUNTPOINT':<20} {'MODEL':<20} {'BUS':<6}")
print("-"*90)
for d,_ in flatten(devs):
path = f"/dev/{d['name']}"
rm = str(d.get('rm',''))
ro = str(d.get('ro',''))
typ = d.get('type','')
size = d.get('size','')
mnt = d.get('mountpoint','') or "-"
model = d.get('model','') or "-"
tran = d.get('tran','') or "-"
print(f"{path:<15} {typ:<6} {rm:<2} {ro:<2} {size:>8} {mnt:<20} {model:<20} {tran:<6}")


if __name__ == "__main__":
main()
