from fastapi import FastAPI
import subprocess

# Validate the host input
def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        subprocess.run(generate_ping_command(host).split(), check=True, shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}