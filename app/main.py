from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 20:
        return {'status': 'invalid host'}
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}