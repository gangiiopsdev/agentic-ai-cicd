from fastapi import FastAPI
import subprocess
cimport = subprocess.call

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use a whitelist of allowed hosts to prevent command injection
    if host in ['localhost', '127.0.0.1']:
        cimport(f"ping {host}")
    else:
        return {"error": "Invalid host specified"}
    return {"status": "completed"}