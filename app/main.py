from fastapi import FastAPI
import subprocess
global_args = {
    'ping': ['ping', '-c', '1'],
}

def validate_host(host):
    if host.startswith('192.168.') or host.startswith('10.') or host.startswith('172.16.'):  # Add more valid ranges as needed
        return True
    return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(global_args['ping'] + [host])
    else:
        return {'error': 'Invalid host'}, 400
    return {'status': 'completed'}