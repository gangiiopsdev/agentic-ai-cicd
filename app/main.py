from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(lambda x: x in allowed_chars, host))

def validate_input(input_value):
    if not input_value:
        return False
    if any(char in input_value for char in [';', '&', '|', '`']):
        return False
    return True

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not validate_input(sanitized_host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {sanitized_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}