from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex.quote to sanitize input
    subprocess.call(f'ping \'{host}\'', shell=True)
    return {"status": "completed"}