from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum():
        return {"status": "error", "message": "Invalid host parameter"}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}