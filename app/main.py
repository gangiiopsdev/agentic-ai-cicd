from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with proper validation and use of subprocess.run
    if not host.strip() or not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}