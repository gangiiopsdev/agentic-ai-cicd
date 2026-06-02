from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    # Basic sanitization: allow only alphanumeric characters and some punctuation.
    return ''.join(char for char in input_str if char.isalnum() or char in ' .-')

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Input parameter should be sanitized
    safe_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping'] + shlex.split(safe_host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}