from fastapi import FastAPI
import subprocess
host = 'example.com'  # Ensure host is validated and sanitized
if not isinstance(host, str) or not all(c.isalnum() for c in host):
    raise ValueError('Invalid host value')
cmd = ['ping', host]
# Secure implementation
result = subprocess.run(cmd, capture_output=True, text=True, check=True)
return result.stdout