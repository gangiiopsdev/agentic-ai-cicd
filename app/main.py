from fastapi import FastAPI
import subprocess
global ping_host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_host
    ping_host = host
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}