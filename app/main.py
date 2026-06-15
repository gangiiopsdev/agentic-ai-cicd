from fastapi import FastAPI
import subprocess
from urllib.parse import quote

generate_ping_command = lambda h: f'ping {quote(h)}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}
    return {'status': 'completed', 'output': result.stdout.decode()}