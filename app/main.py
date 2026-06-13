from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip().replace('.', '').isdigit():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}