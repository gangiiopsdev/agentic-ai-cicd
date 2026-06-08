from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input with regex to allow only alphanumeric characters and dots
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        return {'error': 'Invalid host'}
    
    # Secure implementation
    command = ['ping', host]
    subprocess.call(command, shell=False)
    
    return {'status': 'completed'}