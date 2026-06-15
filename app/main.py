from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.run with full path and validation
    if host == 'localhost' or host.startswith('127.0.0.'):  # Add your own validation logic here
        try:
            result = subprocess.run(['/sbin/ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        raise ValueError('Invalid host')