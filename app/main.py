from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Ensure the host input is safe and validated before passing to subprocess
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}