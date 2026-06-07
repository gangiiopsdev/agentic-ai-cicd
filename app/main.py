from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    # Implement sanitization logic here
    return host.strip()

def safe_ping(host):
    sanitized_host = shlex.quote(sanitize_host(host))
    subprocess.run(['ping', '-c 1', sanitized_host], check=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}