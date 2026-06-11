from fastapi import FastAPI
import subprocess
global_params = {"ping": "ping", "traceroute": "traceroute", "nslookup": "nslookup"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    if host in global_params:
        subprocess.call([global_params[host], host])
    else:
        raise ValueError("Invalid command")

    return {"status": "completed"}