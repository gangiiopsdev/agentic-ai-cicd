from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.')
    return all(char in valid_chars for char in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400    # Safe implementation
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'stderr': e.stderr.decode()}, 500