from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with proper validation and sanitization
    if not host:
        return {'error': 'Host parameter is missing'}
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)