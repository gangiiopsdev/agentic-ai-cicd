from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper argument handling
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}