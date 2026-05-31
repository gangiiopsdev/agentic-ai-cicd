from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

def validate_host(host: str) -> bool:
    if not host.isalnum():
        return False
    if len(host) > 64:
        return False
    return True

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}