from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or 'ping' not in host:
        return False
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.returncode == 0

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "invalid input", "host": host}

    return {"status": "completed"}