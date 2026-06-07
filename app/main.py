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
    try:
        command = f'{global_config['ping_command']} {shlex.quote(host)}'
        output = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}