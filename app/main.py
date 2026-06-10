from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize the host input
    if not host.isalnum():
        raise ValueError('Invalid hostname')

    # Secure implementation with shell=False and full path
    try:
        result = subprocess.run(['/usr/bin/ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize the host input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return ping(host)