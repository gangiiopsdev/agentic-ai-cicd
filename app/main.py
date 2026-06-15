from fastapi import FastAPI
import subprocess
import shlex
import os
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        return {"status": "failed", "error": "Invalid input"}
    args = ['ping', '-c', '1', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}