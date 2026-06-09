from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shell=False and argument list split by shlex
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)
    return {"status": "completed"}