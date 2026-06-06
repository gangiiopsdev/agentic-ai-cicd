from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    # Secure implementation using subprocess.run to safely handle command arguments
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}