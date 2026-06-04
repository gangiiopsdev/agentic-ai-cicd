from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    
    # Use a whitelist of allowed hosts or IPs for security
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError("Host not allowed")
    
    command = ['ping', *shlex.split(host)]
    subprocess.run(command, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}