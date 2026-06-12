from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return secure_ping(host)

def validate_host(host: str):
    # Add validation logic to ensure the host is safe to ping
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts