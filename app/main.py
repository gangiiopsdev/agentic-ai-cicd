from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return shlex.quote(input_string)

def is_valid_host(host):
    # Define a list of allowed hosts or implement more sophisticated validation logic
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host provided')
    # Sanitize the input to prevent command injection
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}