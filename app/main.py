from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not host or not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping'] + shlex.split('-c 1 ' + host), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}