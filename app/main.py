from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)