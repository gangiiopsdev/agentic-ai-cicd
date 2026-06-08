from fastapi import FastAPI
import subprocess
import shlex

global ping
ping = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping
    if ping is None:
        args = shlex.split(f'ping -c 1 {host}')
        ping = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "stdout": ping.stdout.decode(), "stderr": ping.stderr.decode()}