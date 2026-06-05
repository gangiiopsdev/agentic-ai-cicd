from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if os.path.exists('/sbin/ping'):
        subprocess.run(['/sbin/ping', host], check=True)
    else:
        raise Exception('Ping executable not found')
    return {"status": "completed"}