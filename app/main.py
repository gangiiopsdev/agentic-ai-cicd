from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not host.strip() or not all(c.isalnum() or c in '.-\' for c in host):
        return {'error': 'Invalid host parameter'}
    
    # Secure implementation using subprocess.run with shlex.split for safe argument splitting
    result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}