from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(command: str, *args):
    safe_args = [shlex.quote(arg) for arg in args]
    full_command = [command] + safe_args
    try:
        output = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
def ping(host: str):
    # Validate host input to ensure it does not contain malicious content
    if not validate_host_input(host):
        raise ValueError('Invalid host input')
    try:
        output = run_safe_command('ping', host)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
def validate_host_input(host: str) -> bool:
    # Implement validation logic here
    return host.isalnum() or '.' in host@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)