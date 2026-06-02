from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    if not host.strip() or len(host) > 100:
        return False
    return True

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}