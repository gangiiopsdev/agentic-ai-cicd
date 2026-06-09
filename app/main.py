from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not all(c.isalnum() or c in '.-' for c in host):
        return {'status': 'invalid host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}