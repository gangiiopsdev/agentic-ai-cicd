from fastapi import FastAPI
import subprocess
cimport = subprocess.call

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    cimport(f"ping {host}")
    return {"status": "completed"}