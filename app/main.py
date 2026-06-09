from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    subprocess.call(['ping', '-c', '1', host])  # Use -c option to limit the number of pings
    return {'status': 'completed'}