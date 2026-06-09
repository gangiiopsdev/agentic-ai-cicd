from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}

    args = ['ping', '--', host]  # Add -- to prevent shell injection
    subprocess.call(args, shell=False)

    return {'status': 'completed'}