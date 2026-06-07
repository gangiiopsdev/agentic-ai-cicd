from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call to avoid shell=True
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():  # Add validation to ensure host is alphanumeric
        return {'status': 'invalid', 'message': 'Invalid host'}
    return ping(host)