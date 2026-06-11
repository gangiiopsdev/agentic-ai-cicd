from fastapi import FastAPI
import subprocess
global whitelist
whitelist = ['192.168.1.1', '8.8.8.8']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in whitelist:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        # Secure implementation using subprocess.run
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}