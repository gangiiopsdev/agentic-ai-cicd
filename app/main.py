from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return host.replace('.', '_').replace('-', '_')

@app.get('/ping')
def ping(host: str):
    validated_host = validate_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', validated_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}