from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum() or len(host) > 10:
        return False
    return True
def escape_shell_input(input_str):
    # Escape special characters to prevent shell injection
    escaped = input_str.replace(';', ' ').replace('&', ' ')  # Add more as needed
    return escaped
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping'] + shlex.split(escape_shell_input(host)), stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}