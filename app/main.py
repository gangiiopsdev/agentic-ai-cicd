from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    safe_host = subprocess.quote(host)
    args = ['ping', '-c', '1', safe_host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout