from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    # Validate the input to ensure it's a safe hostname
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return ping(host)