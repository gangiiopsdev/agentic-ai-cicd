from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    args = shlex.split(command)
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    command = f'ping {shlex.quote(host)}'
    return run_command(command)