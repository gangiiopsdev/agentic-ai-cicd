from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Secure implementation using shlex.split to safely handle user input
    command = ['ping', host]
    subprocess.run(command, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(shlex.quote(host))
    return {"status": "completed"}