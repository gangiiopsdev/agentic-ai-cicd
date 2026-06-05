from fastapi import FastAPI
import subprocess

app = FastAPI()

gateway = 'ping '

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.call(f'ping {host}')  # Removed shell=True
    return {"status": "completed"}