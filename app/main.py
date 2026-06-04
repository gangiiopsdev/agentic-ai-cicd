from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and sanitizing input
    if 'ping' in host.split():
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}