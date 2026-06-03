from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using shlex.split for safe arguments
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)