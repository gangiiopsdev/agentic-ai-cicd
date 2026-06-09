from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host or len(host) > 255 or not host.replace('.', '').isdigit():
        raise ValueError('Invalid host name')
    # Fixed implementation
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}