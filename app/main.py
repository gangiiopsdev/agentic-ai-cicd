from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip().isdigit():
        args = ['ping', '-c', '1', host]
        return subprocess.call(args, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return None

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result is not None:
        return {"status": "completed", "result": result}
    else:
        return {"status": "failed", "reason": "Invalid host"}