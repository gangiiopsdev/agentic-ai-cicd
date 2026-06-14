from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        command = shlex.split('ping ' + host)
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}