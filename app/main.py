from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.call
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    # Use the safe implementation
    safe_ping(host)

    return {"status": "completed"}