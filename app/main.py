from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(value):
    return ''.join(c if c.isalnum() or c in '-.' else '_' for c in value)

def is_safe_executable(executable):
    safe_executables = ['ping']  # List of allowed executables
    return executable in safe_executables

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not is_safe_executable('ping'):
        return {'status': 'failed', 'error': 'Unsafe executable'}
    try:
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}