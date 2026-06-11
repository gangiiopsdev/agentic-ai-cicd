from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host or ' ' in host:
        raise ValueError('Invalid host input')
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}