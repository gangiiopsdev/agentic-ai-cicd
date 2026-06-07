from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 20:
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", f'"{host}"'])
    return {"status": "completed"}