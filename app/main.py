from fastapi import FastAPI
import subprocess
import shlex

cmd = shlex.split(f'ping {host}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(cmd, check=True)
    return {"status": "completed"}