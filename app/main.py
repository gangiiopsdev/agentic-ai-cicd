from fastapi import FastAPI
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent shell injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['/bin/ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}