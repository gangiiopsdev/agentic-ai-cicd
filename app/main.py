from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host or not host.isalnum():
        return {'status': 'failed', 'message': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}