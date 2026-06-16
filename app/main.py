from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Improved validation logic
    if validate_host(host):
        try:
            result = subprocess.run(['/sbin/ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        raise ValueError('Invalid host')
def validate_host(host: str) -> bool:
    allowed_hosts = ['localhost'] + [f'127.0.0.{i}' for i in range(1, 256)]
    return host in allowed_hosts