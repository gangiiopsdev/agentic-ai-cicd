from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip().endswith('.com') or host.strip().endswith('.org'):
        return False
    return True

@app.get="/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid host")
    return {"status": "completed"}