from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate host input
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host input')
    # Safe implementation using subprocess.run
    cmd = ['ping', shlex.quote(host)]
    result = subprocess.run(cmd, check=True)
    return result.returncode == 0

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if safe_ping(host):
            return {"status": "completed", "response": True}
        else:
            return {"error": "Ping failed", "status": "failed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}