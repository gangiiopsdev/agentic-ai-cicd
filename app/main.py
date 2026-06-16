from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        try:
            output = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        raise ValueError('Invalid host specified')