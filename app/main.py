from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate host input to ensure it contains only allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping {shlex.quote(host)}')
    output = subprocess.run(args, check=True, stdout=subprocess.PIPE)
    return {'status': 'completed', 'output': output.stdout.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}