from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.strip() not in ['127.0.0.1', '::1']:  # Allow only localhost for example purposes
        return {'status': 'denied'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'denied'}
    return safe_ping(host)