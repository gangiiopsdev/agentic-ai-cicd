from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False and proper command specification
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        return {'error': 'Invalid characters in hostname'}, 400
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}