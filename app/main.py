from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", host])

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}