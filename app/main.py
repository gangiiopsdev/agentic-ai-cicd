from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'error': 'Invalid hostname'}

    subprocess.call(['ping', host])

    return {'status': 'completed'}