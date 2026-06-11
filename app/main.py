from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command_parts = ['ping'] + shlex.split(host)
    subprocess.call(command_parts)
    return {'status': 'completed'}