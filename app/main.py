from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.call without shell=True
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    safe_ping(host)

    return {"status": "completed"}