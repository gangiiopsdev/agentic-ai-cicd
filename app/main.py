from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
def validate_host(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host) or len(host.split('.')) != 4:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    success, output = safe_ping(host)
    if success:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'output': output}