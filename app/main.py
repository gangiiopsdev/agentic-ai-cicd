from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        return False
    cmd = ['ping', shlex.quote(host)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}