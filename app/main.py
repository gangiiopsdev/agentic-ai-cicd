from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    if not input_str.isalnum() or '..' in input_str:
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_safe(host: str):
    sanitized_host = sanitize_input(host)
    args = ['/sbin/ping', shlex.quote(sanitized_host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}