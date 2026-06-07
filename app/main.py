from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.Popen
    args = ['ping', host]
    subprocess.Popen(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.Popen
    args = ['ping', host]
    subprocess.Popen(args)

    return {"status": "completed"}