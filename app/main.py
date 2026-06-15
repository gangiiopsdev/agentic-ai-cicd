from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize input
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', host], timeout=10)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)