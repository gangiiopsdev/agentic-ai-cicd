from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "message": "Invalid host"}
    return {"status": "completed"}