from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation
    try:
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Basic regex for hostname validation
            raise ValueError('Invalid host format')
        cmd = ['ping'] + shlex.split(host)
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent injection attacks
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex matching allowed IP addresses and domains
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None