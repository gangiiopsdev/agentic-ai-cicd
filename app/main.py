from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Add comprehensive validation logic here
    valid_hosts = ['example.com', 'test.com']
    return host in valid_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '-c 4', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}