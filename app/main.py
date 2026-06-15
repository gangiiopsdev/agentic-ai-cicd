from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host input')
    # Safe implementation using subprocess.run
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}