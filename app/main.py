from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Safer implementation using subprocess.run with shell=False and input validation
        if not host or len(host) > 255 or not all(c.isalnum() or c in '-.' for c in host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}