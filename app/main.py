from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}