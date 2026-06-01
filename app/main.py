from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.replace('.', '', 3).isdigit():
        return {'status': 'error', 'output': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}