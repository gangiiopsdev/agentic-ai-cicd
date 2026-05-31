from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isdigit() and len(char) <= 15)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host.isdigit() or len(sanitized_host) > 15:
        return {'error': 'Invalid host'}, 400
    subprocess.call(shlex.split(f'ping {sanitized_host}'))
    return {'status': 'completed'}