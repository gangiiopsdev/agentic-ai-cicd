from fastapi import FastAPI
import subprocess
global_params = {"ping": True}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if global_params["ping"] and host == 'example.com':
        subprocess.call(["ping", host])
    return {"status": "completed"}