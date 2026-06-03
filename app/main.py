from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation
    sanitized_host = host.strip()
    if not sanitized_host:
        raise ValueError('Invalid host')
    subprocess.run(['ping', sanitized_host], check=True)
app = FastAPI()
@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get('/ping')
def ping(host: str):