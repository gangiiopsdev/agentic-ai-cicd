from fastapi import FastAPI
import subprocess
from shlex import quote
def ping_safe(host: str):
    # Secure implementation using shlex.quote
    try:
        result = subprocess.run(f'ping {quote(host)}', check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_safe(host: str):
    return ping_safe(host)