from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def ping(host: str):
    # Fixed implementation
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)