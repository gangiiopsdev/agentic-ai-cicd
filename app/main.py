from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        # Secure implementation using subprocess.run
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {"status": "completed"}