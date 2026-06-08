from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not host.strip():
        return None
    try:
        result = subprocess.run(['ping', '--no-hostnames', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    status = safe_ping(host)
    if status is None:
        return {'status': 'Invalid input'}
    return {'status': 'completed', 'output': status}