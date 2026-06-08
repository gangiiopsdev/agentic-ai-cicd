from fastapi import FastAPI
import subprocess
gt from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():
        return {"error": "Invalid input"}, 400
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}