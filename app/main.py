from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize and validate the input
    if not host.isalnum():
        return {'error': 'Invalid hostname'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}