from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.call(args)
    return result

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": status}