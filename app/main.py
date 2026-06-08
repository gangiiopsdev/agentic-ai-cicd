from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it only contains allowed characters
    if not all(c.isalnum() or c in '.-_' for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    
    # Secure implementation using subprocess.run with a safe command list
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}