from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not host.isdigit():
        return {'error': 'Invalid host'}

    # Fixed implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}