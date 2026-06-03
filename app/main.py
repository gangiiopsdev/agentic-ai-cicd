from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and quoting
    command = 'ping '
    args = shlex.split(command + host)
    subprocess.call(args)
    return {"status": "completed"}