from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not re.match(r'^[0-9]{3}$', host) or len(host) != 3:
        return {'status': 'failed', 'error': 'Invalid host format'}
    try:
        result = subprocess.run(['ping', '-c', '1', f'127.0.0.{host}'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}