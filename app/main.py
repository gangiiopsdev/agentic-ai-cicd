from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or '..' in host:
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}