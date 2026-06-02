from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = shlex.quote(host)
    args = ['ping', sanitized_host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent command injection
        return {'status': 'error', 'message': 'Invalid input'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}