from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    subprocess.call(generate_ping_command(host), shell=False)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    # Example: Allow only localhost and example.com
    allowed_hosts = ['localhost', 'example.com']
    return host in allowed_hosts