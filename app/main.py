from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Ensure host is a trusted input
        if not host.isdigit() and '.' not in host and '@' not in host:
            return {'status': 'failed', 'error': 'Invalid host'}
        command_parts = ['ping'] + shlex.split(host)
        return run_safe_command(command_parts)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}