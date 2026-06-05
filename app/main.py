from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation using subprocess.run and shlex.split
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {"status": "completed"}