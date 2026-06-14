from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

def sanitize_input(input_data):
    import re
    cleaned = re.sub(r'[^a-zA-Z0-9.-]', '', input_data)
    return cleaned

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not validate_host(sanitized_host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}