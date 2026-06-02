from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation for host parameter
    if not host.strip() or not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'invalid input'}
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}