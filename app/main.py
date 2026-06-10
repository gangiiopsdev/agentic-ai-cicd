from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = ['example.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}