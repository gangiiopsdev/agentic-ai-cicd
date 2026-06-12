from fastapi import FastAPI
import subprocess
import shlex
global_config = {'ping_enabled': False}
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if not global_config['ping_enabled']:
        return {'error': 'Ping feature is disabled for security reasons.'}, 403
    # Secure implementation using shlex.split and input validation for safe command execution
    try:
        if not host.isdigit():
            raise ValueError('Invalid host format')
        subprocess.call(shlex.split(f'ping {host}'))
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500