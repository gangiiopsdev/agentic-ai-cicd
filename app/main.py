from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host input is sanitized or validated
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(["ping", host], check=True)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}