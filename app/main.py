from fastapi import FastAPI
import subprocess
def safe_subprocess(command_parts):
    for part in command_parts:
        if isinstance(part, str) and '&&' in part or ';' in part or '|' in part:
            raise ValueError('Unsafe characters detected in command input')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_subprocess(['ping', host])
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}