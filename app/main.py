from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent shell injection
    if any(char in host for char in [';', '&', '|', '<', '>', '*', '?', '$', '`']):
        return {'status': 'failed', 'error': 'Invalid characters detected'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}\n
app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return safe_ping(host)