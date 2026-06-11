from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization of input
    if not host.strip():
        return {'status': 'error', 'message': 'Host parameter is required'}
    if '/' in host:
        return {'status': 'error', 'message': 'Invalid host parameter'}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}