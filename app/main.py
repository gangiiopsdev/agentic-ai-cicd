from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' not in host.split():
        return False
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host parameter"}