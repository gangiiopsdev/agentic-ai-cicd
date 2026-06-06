from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use subprocess.run for a safer alternative
        result = subprocess.run(['ping', '-c', '1', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if host.strip() and all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        return {'status': 'completed', 'result': 'Ping successful'}
    else:
        return {'status': 'failed', 'result': 'Invalid input'}