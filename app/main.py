from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.call(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    safe_ping(host)

    return {"status": "completed"}