from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {'status': 'completed'}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)