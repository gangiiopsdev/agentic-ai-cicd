from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {'status': 'invalid_host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}