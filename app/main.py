from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum() or '.' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}