from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}