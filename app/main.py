from fastapi import FastAPI
import subprocess
gimport shlex

gapp = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(shlex.split(f'ping {host}'))

    return {"status": "completed"}