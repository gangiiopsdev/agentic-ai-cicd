from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with additional validation and sanitization
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host name"}
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {"status": "completed"}