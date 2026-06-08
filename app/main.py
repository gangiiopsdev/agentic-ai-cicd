from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isdigit() or len(host) > 15:
        return {'error': 'Invalid input'}
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}