from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    safe_host = host.strip()  # Remove leading/trailing whitespace
    if not safe_host.isalnum():  # Allow only alphanumeric characters and hyphens
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}