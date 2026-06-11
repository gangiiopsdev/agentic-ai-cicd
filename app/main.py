from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric() and len(host) <= 3:
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if safe_ping(host) == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed"}