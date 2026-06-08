from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    command = ['ping'] + shlex.split(host)
    subprocess.call(command, shell=False)

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}