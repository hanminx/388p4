import sys

# Construct the payload: "hanmin" + null terminator + 3 padding bytes + "A+" for grade
payload = b"hanmin" + b"\x00" + b"X" * 3 + b"A+"

# Output the payload as bytes
sys.stdout.buffer.write(payload)
