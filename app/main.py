from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_string):
    return shlex.quote(input_string)

def validate_host(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c 1', f'{sanitized_host}'], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}