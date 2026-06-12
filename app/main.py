from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' in host:
        return None
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result is None:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed', 'output': result}