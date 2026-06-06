from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation
    if ' ' not in host and len(host.split('.')) == 4:
        subprocess.run(["ping", host], check=True)
    else:
        raise ValueError("Invalid host input")
    return {"status": "completed"}