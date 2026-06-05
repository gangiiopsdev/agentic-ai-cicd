from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with proper sanitization
    if host.strip().isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid input for ping host')
    return {'status': 'completed'}