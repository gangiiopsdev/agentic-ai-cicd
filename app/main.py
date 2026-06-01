from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}