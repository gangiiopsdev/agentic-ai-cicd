from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with validation
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}