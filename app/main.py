from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum())

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        raise ValueError('Invalid input. Only alphanumeric characters are allowed.')
    subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True)
    return {'status': 'completed'}