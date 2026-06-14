from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with additional validation
    if not host.isalnum():
        raise ValueError("Invalid input")
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    subprocess.run(command, check=True, text=True)
    return {"status": "completed"}