from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-'
    for char in host:
        if char not in allowed_chars:
            return False
    return len(host) <= 15

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    return {'error': 'Invalid or too long host'}