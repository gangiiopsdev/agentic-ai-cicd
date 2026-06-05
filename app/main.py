from fastapi import FastAPI
import subprocess
def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host name'}
    command = ['ping', host]
    for arg in command:
        if isinstance(arg, str) and '\' in arg:
            return {'status': 'failed', 'error': 'Invalid argument'}
    return run_command(command)