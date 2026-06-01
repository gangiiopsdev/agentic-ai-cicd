from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host) or len(host) > 100:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}