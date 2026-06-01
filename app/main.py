from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Add more allowed hosts as needed
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    try:
        validate_input(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}