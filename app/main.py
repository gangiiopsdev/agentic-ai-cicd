from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input for dangerous characters
    if not host.isalnum() or '&&' in host or ';' in host or '|' in host:
        return {'error': 'Invalid input'}
    try:
        subprocess.run(['ping', quote(host)], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}