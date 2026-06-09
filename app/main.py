from fastapi import FastAPI
import subprocess
host = 'example.com'  # Ensure host is sanitized and validated
try:
    cmd = ['ping', '-c', '1', host]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f'Command failed with error: {e}')