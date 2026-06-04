from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.call with shell=False and input validation
    if not host.isalnum():
        raise ValueError('Invalid host parameter')
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}