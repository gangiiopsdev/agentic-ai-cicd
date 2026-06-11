from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

def run_command(command_parts):
    try:
        output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_input(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid input')

@app.get('/ping')
def ping(host: str):
    try:
        validate_input(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
    command_parts = ['ping', host]
    sanitized_command_parts = [shlex.quote(part) for part in command_parts]
    output = run_command(sanitized_command_parts)
    return {'status': 'completed', 'output': output}