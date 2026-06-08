from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Add logic to validate the host parameter
    allowed_hosts = ['example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {"status": "completed"}