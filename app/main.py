from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.strip()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)