from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or not host.strip():
        return {"error": "Invalid host input"}

    # Secure implementation
    command = shlex.split(f'ping {host}')
    subprocess.call(command)

    return {"status": "completed"}