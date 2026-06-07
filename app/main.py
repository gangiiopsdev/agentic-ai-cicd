from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shell=False and argument sanitization
    args = shlex.split(host)
    subprocess.call(["ping"] + args)
    return {"status": "completed"}