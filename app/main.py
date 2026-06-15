from fastapi import FastAPI
import subprocess

def safe_ping(host):
    if not valid_host(host):
        return False
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return result.stdout

def valid_host(host):
    # Simple validation for demonstration purposes
    return host.isalnum()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    result = safe_ping(host)
    if not result:
        return {"status": "failed", "error": "Ping failed"}
    return {"status": "completed", "result": result}