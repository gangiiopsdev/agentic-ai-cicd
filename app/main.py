from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host and all(c.isalnum() for c in host) and len(host) <= 255:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host input')