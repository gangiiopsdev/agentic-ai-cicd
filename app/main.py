from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate user-provided input to prevent injection attacks
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Unauthorized host'}
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}