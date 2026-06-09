from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and arg splitting
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, timeout=5)
    return {"status": "completed"}