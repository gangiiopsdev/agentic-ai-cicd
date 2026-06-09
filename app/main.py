from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not all(c.isalnum() or c in '.-@' for c in host):
        return {'status': 'error', 'result': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'result': str(e)}