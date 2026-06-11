from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.call without shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    safe_ping(host)

    return {"status": "completed"}