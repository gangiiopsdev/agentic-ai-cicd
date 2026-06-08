from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}