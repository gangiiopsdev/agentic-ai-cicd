from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if 'ping' in host:
        return False
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
        return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'reason': 'Unsafe input'}