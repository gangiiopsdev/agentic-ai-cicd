from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if host.strip() and all(c.isalnum() or c in '-.' for c in host):
        subprocess.run(['ping', host], check=True, capture_output=True)
    else:
        raise ValueError("Invalid input for host")
    return {"status": "completed"}