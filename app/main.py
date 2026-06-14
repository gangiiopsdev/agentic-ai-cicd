from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Use subprocess.run with shell=False and validate input
    if not all(c.isalnum() or c in '.-@' for c in host):
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}