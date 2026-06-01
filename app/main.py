from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and validation of host input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}