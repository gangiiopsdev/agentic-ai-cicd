from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if any(char in host for char in [';', '&', '|', '*', '?', '>', '<', '\\', '$', '`']):
        return {'status': 'error', 'message': 'Invalid characters in host parameter'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}