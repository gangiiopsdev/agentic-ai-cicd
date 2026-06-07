from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def sanitize_input(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Invalid host')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    result = execute_command(command)
    return {'status': 'completed', 'output': result}