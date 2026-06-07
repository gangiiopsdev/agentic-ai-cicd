from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # Define a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return False
    return True

def sanitize_input(input_string):
    # Use regular expression to allow only alphanumeric characters and some special characters
    return re.sub(r'[^a-zA-Z0-9._-]', '', input_string)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not validate_host(sanitized_host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.run(['ping', f'-c 4 {sanitized_host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}