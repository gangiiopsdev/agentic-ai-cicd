from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError('Host cannot be empty')
    try:
        subprocess.run(['ping', host], check=True)
    except Exception as e:
        raise RuntimeError(f'Ping failed for {host}: {e}')