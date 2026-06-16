from fastapi import FastAPI
import subprocess
g import shlex
g 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}