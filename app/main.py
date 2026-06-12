from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.Popen instead of subprocess.call
    args = ['ping', host]
    subprocess.Popen(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen instead of subprocess.call
    args = ['ping', host]
    subprocess.Popen(args)
    return {"status": "completed"}