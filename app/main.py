from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and args parameter
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent shell injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    result = execute_ping(host)
    return result