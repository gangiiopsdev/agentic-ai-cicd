from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or not isinstance(host, str) or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)