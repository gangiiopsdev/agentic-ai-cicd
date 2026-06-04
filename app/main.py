from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host and not any(char in host for char in [';', '&', '|', '`', '$', '#']):
        subprocess.run(["ping", host], check=True, shell=False)
    else:
        raise ValueError("Invalid host")
    return {"status": "completed"}