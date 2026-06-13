from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return run_ping(host)