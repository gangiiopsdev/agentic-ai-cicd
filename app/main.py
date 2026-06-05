from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts
def sanitize_input(input_str):
    sanitized_input = input_str.strip()
    if not all(char.isalnum() or char in '.-' for char in sanitized_input):
        raise ValueError('Invalid characters in input')
    return sanitized_input
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host) or not host:
        return {'error': 'Invalid or missing host'}
    try:
        result = subprocess.run(['ping', '-c', '1', sanitize_input(host)], check=True, text=True, capture_output=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}