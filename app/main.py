from fastapi import FastAPI
import subprocess
import shlex
global_args = {
    'ping': ['ping', '-c', '1'],
}

def validate_host(host):
    if host.startswith('192.168.') or host.startswith('10.') or host.startswith('172.16.'):  # Add more valid ranges as needed
        return True
    return False

def sanitize_input(user_input):
    safe_input = shlex.quote(user_input)
    return safe_input

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(global_args['ping'] + [sanitize_input(host)])
    else:
        return {'error': 'Invalid host'}, 400
    return {'status': 'completed'}