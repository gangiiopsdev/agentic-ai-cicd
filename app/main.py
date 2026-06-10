from fastapi import FastAPI
import subprocess
import shlex

global pinger
pinger = subprocess.Popen(['ping', '-c', '4'], stdout=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    args = shlex.split(f'ping {host}')
    subprocess.run(args)

    return {"status": "completed"}