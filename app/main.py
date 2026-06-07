from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it's safe
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}