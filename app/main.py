from fastapi import FastAPI
import subprocess
import shlex
import os
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host.startswith('-'):  # Prevents command injection by disallowing options
        return {"status": "error", "message": "Invalid host input"}
    args = shlex.split(f"ping {host}")
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}