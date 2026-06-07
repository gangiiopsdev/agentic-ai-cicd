from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation and error handling
    if not host:
        raise ValueError('Host parameter is required')
    try:
        subprocess.run(['ping', '127.0.0.1', f'--{host}'], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}