from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host or not isinstance(host, str) or len(host.split('.')) != 4:
        return False
    return True

cmd = ['ping', '-c', '1', '{}']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}