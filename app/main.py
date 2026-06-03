from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    # Simple sanitization example: allow only alphanumeric characters and hyphens
    return ''.join(char for char in host if char.isalnum() or char == '-').strip()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        args = shlex.split('ping ' + sanitized_host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}