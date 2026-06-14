from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' not in host:
        return False
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "invalid input", "host": host}

    return {"status": "completed"}