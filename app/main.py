from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}