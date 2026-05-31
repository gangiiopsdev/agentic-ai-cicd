from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    try:
        int(host)
        return True
    except ValueError:
        return False

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}