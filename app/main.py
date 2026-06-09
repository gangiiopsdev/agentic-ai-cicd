from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def ping(host: str):
    args = ['ping', host]
    subprocess.run(shlex.split(' '.join(args)), check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}