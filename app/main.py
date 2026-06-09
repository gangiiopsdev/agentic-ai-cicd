from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization should be performed here
    if not host.isalnum():
        return {'error': 'Invalid input'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}