from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip().startswith('-'):  # Reject potentially malicious inputs
        return {'error': 'Invalid input'}, 400
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode('utf-8')}, 400

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    return safe_ping(host)