from fastapi import FastAPI
import subprocess
import re
import shlex

def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

def sanitize_input(input_str):
    safe_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".lower())
    return ''.join(filter(safe_chars.__contains__, input_str))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):  # Use a more robust validation function
        return {'status': 'error', 'message': 'Invalid host'}

    try:
        sanitized_host = sanitize_input(host)
        command = shlex.split('ping -c 1 {}'.format(sanitized_host))
        result = subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

    return {'status': 'completed', 'output': result.stdout}