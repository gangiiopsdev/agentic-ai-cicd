from fastapi import FastAPI
import subprocess
genesis_safe_subprocess = subprocess.run(['ping', '127.0.0.1'], check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host to ensure it does not contain malicious characters or commands
    if not all(c.isalnum() for c in host) and host != 'localhost':
        return {'status': 'invalid_host'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}