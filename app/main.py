from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> bool:
    return all(c.isalnum() or c in ['.', '-', '_'] for c in host)

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}