from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> bool:
    return host.isdigit() and len(host) <= 15

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}