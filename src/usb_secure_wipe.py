#!/usr/bin/env python3
if not confirm("Proceed"):
print("Aborted.")
return


size_bytes = get_device_size_bytes(path)
dev = open_raw_device(path)


try:
device_seek(dev, 0)
if algo == "zeros":
write_full_device(dev, blocksize, "zeros", size_bytes)
expected = 0x00
elif algo == "ones":
write_full_device(dev, blocksize, "ones", size_bytes)
expected = 0xFF
elif algo == "random":
write_full_device(dev, blocksize, "random", size_bytes)
device_seek(dev, 0)
write_full_device(dev, blocksize, "zeros", size_bytes)
expected = 0x00
elif algo == "dod3":
for p in ("zeros","ones","random","zeros"):
device_seek(dev, 0)
write_full_device(dev, blocksize, p, size_bytes)
expected = 0x00
else:
raise ValueError("Unknown algorithm")


print(f"Verifying {samples} random sectors...")
device_seek(dev, 0)
ok = verify_samples(dev, size_bytes, expected, samples=samples)
if ok:
print("VERIFICATION PASSED ✅ — sampled sectors match expected pattern.")
sys.exit(0)
else:
print("VERIFICATION FAILED ❌ — sampled sectors did not match expected pattern.")
sys.exit(3)
finally:
device_close(dev)




def main():
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--device", required=True)
ap.add_argument("--algo", choices=["zeros","ones","random","dod3"], default="dod3")
ap.add_argument("--blocksize", type=int, default=DEFAULT_BLOCK)
ap.add_argument("--verify-samples", type=int, default=64)
ap.add_argument("--yes", action="store_true")
args = ap.parse_args()
if args.blocksize % 512 != 0:
print("Blocksize must be a multiple of 512 bytes.")
sys.exit(1)
run_wipe(args.device, args.algo, blocksize=args.blocksize, samples=args.verify_samples, assume_yes=args.yes)


if __name__ == "__main__":
main()
