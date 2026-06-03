from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in '.-:' for c in host):
        return {'status': 'error', 'output': 'Invalid host'}
    
    # Secure implementation using subprocess.run with shell=False and safe parameters
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)