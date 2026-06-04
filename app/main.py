from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not all(c.isalnum() or c in ('.', '-') for c in host): raise ValueError('Invalid host input')
    # Secure implementation using subprocess.run with shell=False and args parameter
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}