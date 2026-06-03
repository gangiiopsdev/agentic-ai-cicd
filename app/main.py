from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize host input
    if not host.isalnum():
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return safe_ping(host)