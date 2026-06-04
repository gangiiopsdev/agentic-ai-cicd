from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Simple validation to allow only alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host name")