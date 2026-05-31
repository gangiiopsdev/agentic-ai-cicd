from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host or host.strip() == '':
        raise ValueError('Invalid host')
    command = ["ping", host]
    subprocess.run(command, check=True)
    return {"status": "completed"}