from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum() or input_str.startswith('-'):
        raise ValueError('Invalid host name')
    return ''.join(filter(str.isalnum, input_str))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}