from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    valid_hosts = ['127.0.0.1', 'localhost']
    if host not in valid_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}