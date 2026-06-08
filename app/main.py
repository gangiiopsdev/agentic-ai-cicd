from fastapi import FastAPI
import shlex
import subprocess

def execute_command(command: str):
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed with exit code {e.returncode}: {e.stderr}'
global app
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input further
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = 'ping'.split() + [shlex.quote(host)]
    output = execute_command(command)
    return {'status': 'completed', 'output': output}