from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']

def safe_ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)