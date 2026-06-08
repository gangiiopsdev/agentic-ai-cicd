from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement logic to validate the host input
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if is_safe_host(host):
        # Secure implementation
        subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400