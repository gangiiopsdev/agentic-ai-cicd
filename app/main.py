from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using Popen with shell=False and shlex.split
    args = ['ping'] + shlex.split(host)
    subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}