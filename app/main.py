from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str) -> dict:
    # Sanitize the input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '{', '}', '[', ']', '|', '\', ':', ';', '<', '>', ',', '/', '?', '~'])
    try:
        result = subprocess.check_output(['ping', quote(safe_host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode()}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)