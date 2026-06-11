from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    
    # Secure implementation using subprocess.run to avoid shell injection
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}