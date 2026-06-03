from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.TimeoutExpired:
        return {'status': 'timed out'}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'status': 'invalid input'}
    return safe_ping(host)