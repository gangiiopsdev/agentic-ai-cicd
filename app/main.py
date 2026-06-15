from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to escape arguments
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}