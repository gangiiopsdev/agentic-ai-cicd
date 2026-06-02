from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if validate_host(host):
        return safe_ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid host input'}

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed IP ranges or domain names
    allowed_ips = ['192.168.0.1', '10.0.0.1']  # Example list of allowed IPs
    return host in allowed_ips