from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    command_parts = shlex.split('ping -c 1 ' + host)
    output = run_safe_command(command_parts)
    return {'status': 'completed', 'output': output}