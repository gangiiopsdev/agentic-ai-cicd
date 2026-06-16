from fastapi import FastAPI
import subprocess
import shlex
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Sanitize and validate input
    if not host.isalnum():
        return {"status": "invalid input"}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}