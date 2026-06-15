from fastapi import FastAPI
import subprocess
def validate_host(host):
    valid_hosts = ['example.com', 'localhost']
    return host in valid_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, shell=False, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed: {e}', 'output': e.stderr}