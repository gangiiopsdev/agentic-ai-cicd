from fastapi import FastAPI
import subprocess
def run_safe_ping(host):
    if host and not any(char in host for char in ' ;&|<>^()$*?{}[]`~\'"):
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    run_safe_ping(host)
    return {"status": "completed"}