from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation and sanitization
    if not host.replace('.', '', 3).isdigit():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        subprocess.run(['ping', '-c', '4', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}