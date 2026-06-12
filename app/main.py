from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with argument escaping
    if all(c.isalnum() or c in ['.', '-'] for c in host):
        subprocess.call(['ping', host])
    return {'status': 'completed'}