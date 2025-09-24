# USB Secure Wipe Tool


Cross-platform Python utility to securely erase USB pendrives by overwriting raw device blocks. Implements multiple wipe algorithms, verification sampling, and safety checks.


## Features
- Algorithms: `zeros`, `ones`, `random`, `dod3` (DoD 3-pass style)
- Cross-platform raw device access (Linux `/dev/sdX`, Windows `\\.\PhysicalDriveN`)
- Verification via random-sector sampling
- Simple CLI interface


## Quickstart


1. Clone the repo
```bash
git clone https://github.com/vishruthmh/USB-Secure-Wipe-Tool
cd usb-secure-wipe
sudo python3 src/usb_secure_wipe.py --device /dev/sdb --algo dod3 --verify-samples 64
