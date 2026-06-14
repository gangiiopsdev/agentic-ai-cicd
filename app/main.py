from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Safe implementation using subprocess.run with proper validation and sanitization
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    command = ['ping', '-c', '1'] + [shlex.quote(arg) for arg in host.split()]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    return all(c.isalnum() or c in ['-', '.'] for c in host)