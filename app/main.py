from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}