from fastapi import FastAPI
import subprocess
host = 'example.com'  # Ensure host is sanitized and validated
try:
    if '@' in host or '&' in host or '|' in host or ';' in host:
        raise ValueError('Invalid host input')
    cmd = ['ping', '-c', '1', shlex.quote(host)]  # Use shlex.quote to sanitize the host input
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f'Command failed with error: {e}')