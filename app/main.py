from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.strip().isdigit():
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}