from fastapi import FastAPI
import subprocess
import re
import shlex

def sanitize_input(user_input):
    return ''.join(ch if ch.isalnum() or ch in '.-' else '_' for ch in user_input)

def validate_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate user input
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}