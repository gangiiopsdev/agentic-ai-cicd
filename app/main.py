from fastapi import FastAPI
import subprocess

generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it's a valid hostname or IP address
    if not host.isdigit() and not '.' in host:
        raise ValueError('Invalid input for host. Only numeric IPs and domain names are allowed.')
    command = generate_ping_command(host)
    result = subprocess.run(command, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}