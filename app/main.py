from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 10

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if not sanitize_host(host):
        return {"status": "failed", "error": "Invalid host name"}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}