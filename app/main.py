from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize host input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)