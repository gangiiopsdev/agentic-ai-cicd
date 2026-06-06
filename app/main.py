from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'status': 'failed'}

app = FastAPI()

@app.get('/ping')
def ping_handler(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid hostname', 'status': 'failed'}
    return ping(host)