from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    command = 'ping {}
    args = shlex.split(command)
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}