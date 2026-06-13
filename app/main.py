from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate host input before using it in a subprocess call
    if not host.strip().isdigit():
        raise ValueError('Invalid host input')
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}