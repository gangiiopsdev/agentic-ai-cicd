from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = {'example.com', 'test.com'}
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}