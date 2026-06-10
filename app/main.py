from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote to safely handle user input
    command = f'ping {shlex.quote(host)}'
    subprocess.call(command, shell=True)

    return {"status": "completed"}