from fastapi import FastAPI
import subprocess
global args
args = []

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global args
    args.append(f'ping {host}')
    return {"status": "completed"}