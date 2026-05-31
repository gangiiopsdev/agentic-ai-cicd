from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shlex.split to split the command safely
    import shlex
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {"status": "completed"}