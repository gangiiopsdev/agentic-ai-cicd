from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    return execute_ping(sanitized_host)

def is_valid_host(host):
    # Implement validation logic to ensure the host is safe to ping
    pass

def sanitize_input(input_string):
    # Implement input sanitization logic to prevent OS command injection
    import re
    allowed_chars = re.compile(r'^[a-zA-Z0-9.-]+$')
    return allowed_chars.match(input_string) and input_string