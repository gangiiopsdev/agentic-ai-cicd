from fastapi import FastAPI
import subprocess
from typing import Optional
def validate_host(host: str) -> bool:
    try:
        int(host)
        return True
    except ValueError:
        return False
app = FastAPI()
@app.get('/ping')
def ping(host: Optional[str] = None):
    if not host or not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}