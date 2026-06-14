from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.startswith('-'):
        raise ValueError('Invalid hostname provided.')
    subprocess.call(['ping', '-c', '1', host])  # Limiting the number of pings to one for security
    return {"status": "completed"}