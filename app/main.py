from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())

def validate_and_sanitize_host(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname provided')
    return sanitize_input(host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = validate_and_sanitize_host(host)
    subprocess.run(shlex.split(f'ping -c 4 {sanitized_host}'), check=True, shell=False)
    return {'status': 'completed'}