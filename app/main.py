from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return subprocess.call(['ping', host], capture_output=True, text=True)

@app.get="/ping")
def ping(host: str):
    # Secure implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}