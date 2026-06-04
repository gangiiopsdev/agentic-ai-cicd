from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    return '.' in host and len(host.split('.')) == 4 and all(c.isdigit() for c in host.replace('.', ''))

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}