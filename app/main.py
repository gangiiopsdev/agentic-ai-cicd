from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.replace('.', '', 2).isdigit() or '@' in host:
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"status": "invalid_host"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)