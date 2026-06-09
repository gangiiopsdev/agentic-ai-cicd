from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host and all(c in string.ascii_letters + string.digits for c in host):
        subprocess.run([os.path.join('/', 'bin', 'ping'), host], check=True)
    else:
        raise ValueError('Invalid input for ping')
    return {"status": "completed"}