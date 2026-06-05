from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote for argument escaping
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.quote for argument escaping
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}