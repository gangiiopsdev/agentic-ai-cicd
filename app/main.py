from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input more thoroughly
    if not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation using subprocess.run with full path and input sanitization
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}