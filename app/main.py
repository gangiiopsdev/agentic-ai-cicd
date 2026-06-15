from fastapi import FastAPI
import subprocess
global_ping_hosts = {"example.com": None} # Define allowed hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in global_ping_hosts:
        subprocess.call(f"ping {host}", shell=True)
    else:
        return {"status": "Error", "message": "Host not allowed"}
    
    return {"status": "completed"}