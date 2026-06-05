from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.strip() or '..' in host or '/' in host or '\' in host:
        raise ValueError('Invalid host input')
    return host.strip()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validated_host = validate_host(host)
        result = subprocess.run(['ping', '-c', '1', validated_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}