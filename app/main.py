from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host:
        raise ValueError('Host parameter cannot be empty')
    command = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    return safe_ping(host)