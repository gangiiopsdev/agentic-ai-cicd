from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize host input
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])