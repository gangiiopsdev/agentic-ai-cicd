from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": subprocess.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.stderr.decode())}