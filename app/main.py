from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.split to safely handle user input
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}