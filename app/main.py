from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = sp.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}