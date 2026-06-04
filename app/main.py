from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not is_valid_host(host):
        return "Invalid host"
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

def is_valid_host(host: str) -> bool:
    # Basic validation of the host input
    return all(c.isalnum() or c in '.-' for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": status}