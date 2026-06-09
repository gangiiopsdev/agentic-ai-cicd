from fastapi import FastAPI
import subprocess
from shlex import quote


global_config = {
    'ping': {
        'command': ['ping', '{}'],
    }
}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_host = quote(host)
        command = global_config['ping']['command'].format(safe_host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5, shell=False)  # Changed shell=True to False
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}