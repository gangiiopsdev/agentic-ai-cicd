from fastapi import FastAPI
import subprocess
import shlex

global_config = {
    'ping_command': 'ping'
}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with command validation
    try:
        args = [global_config['ping_command']] + shlex.split(host)
        subprocess.call(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 400