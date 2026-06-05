from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}