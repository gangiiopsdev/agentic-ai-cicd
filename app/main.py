from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '--', host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}
def is_valid_host(host: str) -> bool:
    # Add validation logic here
    valid_hosts = ['example.com', 'test.com']
    return host in valid_hosts