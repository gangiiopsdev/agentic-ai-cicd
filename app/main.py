from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}