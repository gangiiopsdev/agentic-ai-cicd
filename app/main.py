from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return ping(host)

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Define allowed hosts
    return host in allowed_hosts