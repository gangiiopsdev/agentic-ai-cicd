from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host):
    ping_cmd = ['ping', host]
    subprocess.call(ping_cmd)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}