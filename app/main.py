from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    args = ['ping', quote(host)]
    subprocess.call(args)

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}