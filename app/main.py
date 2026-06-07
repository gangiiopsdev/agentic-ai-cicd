from fastapi import FastAPI
import subprocess
import re
import shlex

def validate_host(host):
    expected_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in expected_chars for char in host)

def sanitize_input(input_str):
    # Add more sophisticated input sanitization if necessary
    return ''.join(filter(lambda x: x.isalnum() or x in '.-', input_str))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}