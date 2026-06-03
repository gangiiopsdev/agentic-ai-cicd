from fastapi import FastAPI
import subprocess

def safe_ping(host):
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid input for host')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input more strictly to prevent command injection
    if not host.isdigit() and not any(char.isalpha() for char in host):  # Example validation
        raise ValueError('Invalid input for host')
    return safe_ping(host)