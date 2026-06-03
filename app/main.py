from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or '-' in host:
        return {'error': 'Invalid input'}, 400
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}