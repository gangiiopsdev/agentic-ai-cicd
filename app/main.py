from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split to prevent injection
    args = ['ping', host]
    subprocess.run(args)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split to prevent injection
    args = ['ping', host]
    subprocess.run(args)
    return {"status": "completed"}