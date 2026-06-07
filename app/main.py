from fastapi import FastAPI
import subprocess
g-import shlex
g
app = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}