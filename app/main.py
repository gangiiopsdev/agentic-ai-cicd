from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation using shlex.split for safe command argument parsing
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    secure_ping(host)
    return {"status": "completed"}