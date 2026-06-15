from fastapi import FastAPI
import subprocess
gimport shlex
gimport os
g
app = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    
    return {"status": "completed"}