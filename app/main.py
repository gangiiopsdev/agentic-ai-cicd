from fastapi import FastAPI
import subprocess
from typing import Tuple, Optional

def safe_ping(host: str) -> Tuple[Optional[str], Optional[str]]:
    # Using subprocess.run with a list to avoid shell injection and validating input
    if not host or '&&' in host or ';' in host or '|' in host or '`' in host:
        return None, 'Invalid input'
    try:
        result = subprocess.run(['ping', '-c', str(1), host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode(), None
    except subprocess.CalledProcessError as e:
        return None, str(e.stderr.decode())

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with error handling and input validation
    output, errors = safe_ping(host)
    if errors:
        return {'status': 'error', 'output': None, 'errors': errors}
    else:
        return {'status': 'completed', 'output': output}