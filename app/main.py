from fastapi import FastAPI
import subprocess
from urllib.parse import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input for dangerous characters and length
    if not host.isalnum() or len(host) > 255 or '&&' in host or ';' in host or '|' in host:
        return {'error': 'Invalid input'}
    try:
        subprocess.run(['ping', f'-c 1 {quote(host)}'], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}