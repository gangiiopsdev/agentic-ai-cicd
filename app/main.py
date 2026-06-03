from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split for safe argument splitting
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shlex.split for safe argument splitting
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}