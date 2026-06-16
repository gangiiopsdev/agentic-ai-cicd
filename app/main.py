from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = f'ping {shlex.quote(host)}'
    subprocess.call(command, shell=False)
    return {"status": "completed"}