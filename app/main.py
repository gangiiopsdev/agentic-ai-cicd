from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts