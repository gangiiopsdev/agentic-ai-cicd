from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    return '127.0.0.1' if host == 'ping' else host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        output = subprocess.run(['ping', '-c', '1', '--', sanitized_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}