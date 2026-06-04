from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host to ensure it does not contain malicious characters or commands
    if not all(c.isalnum() for c in host) and host != 'localhost':
        return {'status': 'invalid_host'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}