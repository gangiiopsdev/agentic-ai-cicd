from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip().isdigit():
        return subprocess.call(['ping', '-c', '1', host], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return None

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result is not None:
        return {"status": "completed", "result": result}
    else:
        return {"status": "failed", "reason": "Invalid host"}