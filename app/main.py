from fastapi import FastAPI
import subprocess
global_host = "127.0.0.1"  # Example default host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str = global_host):
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}