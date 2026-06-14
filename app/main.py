from fastapi import FastAPI
import subprocess
def safe_host(host: str) -> str:
    allowed_hosts = ['ping', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str = 'localhost'):  # Use a default safe value
    try:
        sanitized_host = safe_host(host)
        output = subprocess.run([sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}