from fastapi import FastAPI
import shlex
import re
def sanitize_input(input_string):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, input_string))
def validate_host(host):
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    return safe_ping(sanitized_host)