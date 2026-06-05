from fastapi import FastAPI
import subprocess
import shlex
global app
global host_value

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(shlex.split(f"ping {host}"))
    return {'status': 'completed'}