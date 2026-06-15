from fastapi import FastAPI
import subprocess
g import shlex
def safe_ping(host: str):
    cmd = ['ping', host]
    args = list(shlex.split(' '.join(cmd)))
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}