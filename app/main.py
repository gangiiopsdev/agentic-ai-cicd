from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., allow only specific domains or IP addresses
    allowed_hosts = ['example.com', '192.168.1.1']
    return host in allowed_hosts