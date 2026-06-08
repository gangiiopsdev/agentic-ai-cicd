from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        return {'status': 'completed'} if ping(host) else {'status': 'failed'}
    except Exception as e:
        return {'error': str(e)}