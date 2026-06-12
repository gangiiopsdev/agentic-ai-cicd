from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host parameter
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'error': 'Invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}