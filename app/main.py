from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run with proper validation
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', '-c', '1', host], check=True)

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    return all(c.isalnum() or c in ['-', '.'] for c in host)