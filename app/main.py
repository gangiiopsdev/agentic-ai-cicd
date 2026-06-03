from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip().replace(' ', '').replace('\', '')
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}