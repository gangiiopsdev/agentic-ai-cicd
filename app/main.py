from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}