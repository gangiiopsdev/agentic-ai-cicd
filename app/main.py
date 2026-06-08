from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    if isinstance(host, str) and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return f'ping {host}'
    else:
        raise ValueError('Invalid host input')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        command = generate_ping_command(host)
        subprocess.run(command.split(), shell=False, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}