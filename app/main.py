from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ['.', '-', '_'])

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = shlex.split(f'ping {sanitized_host}')
    try:
        result = subprocess.run(command, check=True, shell=False, capture_output=True, timeout=10)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}