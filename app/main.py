from fastapi import FastAPI
import subprocess
def run_ping(host):
    if not host.isalnum():
        return {"error": "Invalid host name"}
    subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    return run_ping(host)