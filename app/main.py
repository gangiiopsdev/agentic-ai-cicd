from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}