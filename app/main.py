from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safer implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.replace('.', '').isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    return run_ping(host)