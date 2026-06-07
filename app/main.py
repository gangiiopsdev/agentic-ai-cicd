from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and sanitized input
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):   
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}