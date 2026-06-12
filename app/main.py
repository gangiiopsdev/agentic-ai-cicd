from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    subprocess.call(shlex.split(f"ping {host}"))
    return {'status': 'completed'}