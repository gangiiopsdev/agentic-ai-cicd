from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the host to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)