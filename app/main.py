from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['localhost', '127.0.0.1']:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"status": "denied", "reason": "Unsafe host"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)