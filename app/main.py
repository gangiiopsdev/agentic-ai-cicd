from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 50:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', '-c', '1', f'"{host}"'])
    return {'status': 'completed'}