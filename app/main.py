from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError('Invalid host name')

@app.get="/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', safe_ping(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}