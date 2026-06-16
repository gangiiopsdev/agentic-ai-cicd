from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and arg substitution
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and arg substitution
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)
    return {"status": "completed"}