from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {'status': 'invalid_host'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}