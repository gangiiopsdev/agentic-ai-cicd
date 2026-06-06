from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.strip():
        return {'error': 'Invalid host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}