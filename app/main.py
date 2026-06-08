from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host not in ['example.com', 'test.com']:
        return {'status': 'error', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)