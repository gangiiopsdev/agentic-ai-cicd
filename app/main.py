from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    if not host.replace('.', '').isdigit() or len(host.split('.')) != 4:
        return None
    return host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is None:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}