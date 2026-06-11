from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host in ['localhost', '127.0.0.1']:
        subprocess.run(['ping', '-c', '1', host], check=True)
    else:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        response = ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}