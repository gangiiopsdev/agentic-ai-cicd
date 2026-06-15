from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host and all(c.isalnum() or c in ('.', '-') for c in host):
        subprocess.run(['ping', host], check=True, text=True)
    else:
        raise ValueError('Invalid hostname')
    return {"status": "completed"}