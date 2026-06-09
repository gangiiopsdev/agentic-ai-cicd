from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> dict:
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Unauthorized host'}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)