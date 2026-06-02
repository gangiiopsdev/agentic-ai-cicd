from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        raise ValueError(f'Ping failed with error code {e.returncode}')

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}