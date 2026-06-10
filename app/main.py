from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    try:
        # Validate and sanitize the input to prevent command injection
        if not host.replace('.', '').replace('-', '').isalnum():
            raise ValueError("Invalid hostname")
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, ValueError) as e:
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Ping failed'}
    return {'status': 'completed'}