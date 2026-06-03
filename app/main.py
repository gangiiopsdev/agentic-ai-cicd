from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation and sanitization
    if not all(c.isalnum() or c in '.:-_' for c in host):
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}