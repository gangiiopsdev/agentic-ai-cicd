from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using subprocess.run with check=True and sanitized input
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    sanitized_host = ''.join(char for char in host if char.isalnum() or char in ['.', '-'])
    return ping(sanitized_host)