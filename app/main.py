from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=10)
        return {"status": "completed", "output": output.decode()} 
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}

def is_valid_host(host: str) -> bool:
    # Simple validation, replace with more robust logic if needed
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts