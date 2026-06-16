from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation
    if host and len(host.split('.')) == 4:
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid hostname'}, 400