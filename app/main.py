from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum())

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'error': 'Invalid input'}, 400
    args = ['ping', shlex.quote(sanitized_host)]
    subprocess.call(args)
    return {'status': 'completed'}