from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Fixed implementation
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'Ping successful' if result.returncode == 0 else 'Ping failed'}

def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'Ping successful' if result.returncode == 0 else 'Ping failed'}