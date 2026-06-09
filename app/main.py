from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_safe_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return all(char in allowed_chars for char in hostname)

def validate_input(input_string):
    # Regular expression to allow only safe characters and patterns
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, input_string) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_input(host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', f'--{host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}