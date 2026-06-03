from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to avoid command injection
    if not host.isalnum():
        return {'status': 'invalid input'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}