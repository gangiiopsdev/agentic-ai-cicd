from fastapi import FastAPI
import subprocess
global pings = set()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in pings:
        pings.add(host)
        subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}