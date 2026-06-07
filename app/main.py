from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with proper validation
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    subprocess.call(['ping', host])
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement your validation logic here
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts