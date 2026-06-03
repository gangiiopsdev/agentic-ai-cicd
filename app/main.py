from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using check_output to avoid shell injection
    if host.startswith('/') or '..' in host:
        raise ValueError('Invalid host parameter')
    result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
    return {'status': 'completed', 'output': result}