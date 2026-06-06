from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate and sanitize input
    if not host or len(host) > 255:
        return {'error': 'Invalid host'}
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def secure_ping(host: str):
    return ping(host)