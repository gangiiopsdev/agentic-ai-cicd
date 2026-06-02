from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric() and '-' not in host and '/' not in host:
        command_parts = ['ping', shlex.quote(host)]
        try:
            output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'invalid_host', 'message': 'Invalid host provided'}