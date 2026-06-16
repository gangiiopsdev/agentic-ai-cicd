from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation using shlex.split for argument splitting
    cmd_parts = ['ping'] + shlex.split(host)
    subprocess.call(cmd_parts)

@app.get("/ping")
def ping(host: str):    ping_safe(host)    return {"status": "completed"}