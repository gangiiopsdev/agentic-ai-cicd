from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the hostname
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['ping', '-c', '1', f'--nameserver {host}'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}