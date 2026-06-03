from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input
    if not host.isalnum():
        return {'error': 'Invalid input'}
    
    # Fixed implementation with shell=False to prevent shell injection
    subprocess.call(['ping', host], shell=False)
    
    return {'status': 'completed'}