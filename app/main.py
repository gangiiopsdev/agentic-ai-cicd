from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and escaping
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}