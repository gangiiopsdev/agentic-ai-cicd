from fastapi import FastAPI
import subprocess
global completed
completed = False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global completed
    if not completed:
        subprocess.call(f"ping {host}", shell=True)
        completed = True
    return {"status": "completed"}