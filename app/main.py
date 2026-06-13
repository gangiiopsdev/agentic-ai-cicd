from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ["example.com", "another.example.com"]:
        subprocess.call(["ping", host])
        return True
    else:
        raise ValueError("Invalid host")
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(")
def ping(host: str):
    try:
        if safe_ping(host):
            return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}