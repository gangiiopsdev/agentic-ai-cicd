from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        return {'error': 'Invalid host input'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}