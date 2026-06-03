from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not all(c.isalnum() or c in ['-', '.', '_', ','] for c in host):
        raise ValueError('Invalid characters in host parameter')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}