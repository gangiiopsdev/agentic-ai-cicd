from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isdigit():
        return {'error': 'Invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}