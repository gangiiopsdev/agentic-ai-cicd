from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host.isalnum():
        return {'error': 'Invalid input'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}