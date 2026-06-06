from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host input is sanitized or validated
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(["ping", f'-c 1 {host}'], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}