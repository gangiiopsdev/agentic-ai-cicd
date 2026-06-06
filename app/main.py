from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.isnumeric() and len(host) <= 4:
        args = ['ping', host]
        subprocess.call(args)
    return {"status": "completed"}