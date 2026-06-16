from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with absolute path and validation of input
    if not host.isdigit() or len(host) > 15:
        raise ValueError("Invalid host format")
    command = "/bin/ping {}
    args = shlex.split(command)
    subprocess.run(args, check=True)
    return {"status": "completed"}