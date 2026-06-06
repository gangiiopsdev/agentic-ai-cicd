from fastapi import FastAPI
import subprocess
import shlex

global_params = {
    "ping": "/usr/bin/ping",
}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = [global_params['ping'], host]
    subprocess.run(command, check=True)
    return {"status": "completed"}