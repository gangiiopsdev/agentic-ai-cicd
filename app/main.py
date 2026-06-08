from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'invalid input'}
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}