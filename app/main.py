from fastapi import FastAPI
import subprocess
def execute_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.strip() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    command_parts = ['ping', host]
    return execute_safe_command(command_parts)