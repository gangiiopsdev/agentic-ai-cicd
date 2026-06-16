from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}