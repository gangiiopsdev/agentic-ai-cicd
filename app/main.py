from fastapi import FastAPI
import subprocess
from shlex import quote

global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = quote(host)
    args = ['ping', safe_host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}