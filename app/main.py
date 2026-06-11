from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):\n    validate_host(host)\n    command = ['ping', host]\n    result = subprocess.run(command, check=True, capture_output=True, text=True)\n    return {'status': 'completed', 'output': result.stdout}