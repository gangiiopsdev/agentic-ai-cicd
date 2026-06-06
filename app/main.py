from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not host.isalnum():
        return {'error': 'Invalid host'}
    
    # Secure implementation
    subprocess.call(['ping', host])
    
    return {'status': 'completed'}