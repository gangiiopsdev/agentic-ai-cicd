from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.startswith('192.168.') or host.startswith('localhost'):  # Example of simple validation
        subprocess.call(['ping', host])
    return {'status': 'completed'}