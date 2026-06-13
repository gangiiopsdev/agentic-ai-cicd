from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    cmd = ['ping', host]
    subprocess.call(cmd, shell=False)
    return {'status': 'completed'}