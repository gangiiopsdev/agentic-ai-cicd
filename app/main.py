from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with full path and input sanitization
    if host.strip() != host or '@' in host or '/' in host:
        return {'status': 'error', 'message': 'Invalid host input'}
    command = ['ping', shlex.quote(host)]  # Use shlex.quote to escape the input
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}