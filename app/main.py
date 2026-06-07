from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ' '.join(shlex.split(input_string))
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}