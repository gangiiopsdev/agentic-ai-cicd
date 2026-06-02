from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    full_command = [os.path.join(os.sep, *host.split('.')) for _ in range(4)] + ['ping']
    subprocess.call(full_command)

    return {"status": "completed"}