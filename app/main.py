from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if '.' not in host and '@' not in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    command = ['ping', '-c 1', host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isdigit() and '@' not in host and '.' not in host and len(host) < 256:
            return safe_ping(host)
        else:
            return {'status': 'failed', 'error': 'Invalid host'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}