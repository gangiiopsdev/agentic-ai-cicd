from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list of arguments
    subprocess.run(['ping', host])

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent injection
        return {'status': 'error', 'message': 'Invalid input'}
    safe_ping(host)
    return {'status': 'completed'}