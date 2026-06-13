from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Validate and sanitize the input to prevent injection attacks
    if not sanitized_host.isalnum() or len(sanitized_host) > 255:
        raise ValueError('Invalid hostname provided')
    subprocess.run(shlex.split(f'ping -c 4 {sanitized_host}'), check=True, shell=False)
    return {'status': 'completed'}