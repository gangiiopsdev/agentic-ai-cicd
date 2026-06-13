from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    sanitized_host = shlex.quote(host)
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'output': result.stdout}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here (e.g., IP address format, domain name length)
    return True