from fastapi import FastAPI
import subprocess
import shlex
gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ["127.0.0.1", "localhost"]
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}

    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}