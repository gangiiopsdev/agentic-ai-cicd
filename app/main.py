from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run instead and avoid shell=True
    args = ['ping', host]
    args = [shlex.quote(a) for a in args]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the input to prevent injection attacks
        if not os.path.basename(host).isalnum() or len(host) > 255:
            raise ValueError("Invalid host name")
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}