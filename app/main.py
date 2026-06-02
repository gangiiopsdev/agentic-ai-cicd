from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char if char in allowed_chars else '_' for char in user_input)
    return sanitized

def validate_host(host):
    # Add validation logic here, e.g., allow only specific hosts or domains
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(shlex.split(f'ping {sanitized_host}'), stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}