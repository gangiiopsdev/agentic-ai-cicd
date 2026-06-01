from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or '..' in host:
        raise ValueError("Invalid hostname")
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}