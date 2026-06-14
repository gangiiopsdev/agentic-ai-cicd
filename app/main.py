from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', '192.168.1.1']
    return host in allowed_hosts
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        command = ['ping', '--count=1', host]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}