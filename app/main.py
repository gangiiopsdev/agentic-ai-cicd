from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'localhost']

def sanitize_input(input_str):
    # Regex to allow only alphanumeric characters and hyphens
    if re.match(r'^[a-zA-Z0-9-]+$', input_str):
        return input_str
    else:
        raise ValueError('Invalid input')

@app.get('/ping')
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', sanitize_input(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}