from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() and all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        subprocess.run(['ping', host], check=True, shell=False)
    else:
        raise ValueError('Invalid host provided')
    return {"status": "completed"}