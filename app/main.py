from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host) and len(host) <= 50

@app.get('/ping')
def ping(host: str):
    if not safe_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True for security reasons
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}