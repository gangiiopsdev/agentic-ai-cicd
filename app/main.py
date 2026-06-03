from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.strip():
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}