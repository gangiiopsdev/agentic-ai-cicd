from fastapi import FastAPI
import subprocess
import shlex

global host_var = "example.com"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command_parts = shlex.split(f'ping {host}')
    subprocess.call(command_parts, shell=False)
    return {"status": "completed"}