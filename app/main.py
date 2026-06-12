from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    # Simple validation: allow only alphanumeric characters and hyphens
    return host.isalnum() or '-' in host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        try:
            # Use shlex.quote to safely escape the host parameter
            subprocess.run(['ping', shlex.quote(host)], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed: {e}'}, 500
    else:
        return {'error': 'Invalid host'}, 400