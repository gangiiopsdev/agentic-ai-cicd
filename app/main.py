from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)