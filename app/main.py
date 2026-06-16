from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation using subprocess.run and list
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '4', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}