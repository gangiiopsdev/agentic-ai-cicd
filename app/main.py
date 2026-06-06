from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)