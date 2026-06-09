from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))[:255]
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError('Invalid host input')
    command = ['ping', '-c', '1', shlex.quote(sanitized_host)]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}