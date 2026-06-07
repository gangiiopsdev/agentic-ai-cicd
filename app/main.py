from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using Popen without shell=True
    ping_cmd = ['ping', host]
    subprocess.Popen(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}