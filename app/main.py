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
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}