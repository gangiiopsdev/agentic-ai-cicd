from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError('Invalid hostname')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        # Use shlex to safely quote arguments
        subprocess.run(['ping', '-c', '1', shlex.quote(host)], check=True)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'error': str(e)}