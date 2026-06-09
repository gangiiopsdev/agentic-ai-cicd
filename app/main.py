from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    allowed_hosts = ["example.com", "another.example.com"]
    return host in allowed_hosts