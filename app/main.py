from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(e for e in host if e.isalnum() or e in ['.', '-'])

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}