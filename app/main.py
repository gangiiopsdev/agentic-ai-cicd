from fastapi import FastAPI
import subprocess

allowed_hosts = ['example.com', '192.168.1.1']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        command = ['ping', '--count=1', host]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}