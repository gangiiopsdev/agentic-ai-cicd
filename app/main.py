from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input
    if not host or not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host input'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)