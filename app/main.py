from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure the host parameter is sanitized and valid
    if not host or not host.strip():
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}