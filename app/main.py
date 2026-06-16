from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid hostname'}
    sanitized_host = ''.join(c for c in host if c.isalnum())  # Sanitize input to allow only alphanumeric characters
    result = subprocess.run(['ping', '-c', '1', shlex.quote(sanitized_host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Additional security measure: Validate sanitized_host further if necessary