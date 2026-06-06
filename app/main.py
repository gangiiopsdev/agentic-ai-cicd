from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host or 'localhost' in host.lower():
        return {'error': 'Invalid host'}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}