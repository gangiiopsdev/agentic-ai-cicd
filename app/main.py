from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation using subprocess.run with a list of arguments instead of a single string.
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    ping_safe(host)
    return {"status": "completed"}