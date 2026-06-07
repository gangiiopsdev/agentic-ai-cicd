from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip():
        raise ValueError("Invalid host provided")
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}