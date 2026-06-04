from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    safe_ping(host)
    return {'status': 'completed'}