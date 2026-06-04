from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Add logic to validate the host input
    return True

@app.get('/ping')
def ping(host: str):
    if is_safe_host(host):
        # Secure implementation using subprocess.run with shell=False and args parameter
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400