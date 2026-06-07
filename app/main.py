from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ('.', '-', '_'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', '--', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

# Add input validation and sanitization for `host`
def validate_host(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(char in allowed_chars for char in host): raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    safe_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', '--', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}