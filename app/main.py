from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host: str):
    if not host.isalnum() or len(host) > 255:
        return False
    return True

def execute_command(command_parts: list):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid input'}
    try:
        host = shlex.quote(host)
        command_parts = ['ping', '-c', '1', os.path.abspath(host)]
        return execute_command(command_parts)
    except Exception as e:
        return {'status': 'error', 'output': str(e)}