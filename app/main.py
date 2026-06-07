from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Add validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}