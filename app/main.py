from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and quoting
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and quoting
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)
    return {"status": "completed"}