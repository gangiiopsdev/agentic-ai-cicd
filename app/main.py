from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation using subprocess.run without shell=True and input validation
    if not host or ' ' in host:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}