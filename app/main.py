from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with validation
    if not host.strip().isalnum() or len(host) > 255:
        return {'error': 'Invalid input'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}