from fastapi import FastAPI
import subprocess

def validate_host(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host) or len(host.split('.')) != 4:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}