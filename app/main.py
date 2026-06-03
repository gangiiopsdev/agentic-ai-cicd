from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.split for safe argument splitting
    args = shlex.split('ping ' + host)
    subprocess.call(args, shell=False)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.split for safe argument splitting
    args = shlex.split('ping ' + host)
    subprocess.call(args, shell=False)
    return {"status": "completed"}