from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

def validate_host(host):
    if not host.replace('.', '', 3).isdigit():
        raise ValueError('Invalid host format')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    return safe_ping(host)