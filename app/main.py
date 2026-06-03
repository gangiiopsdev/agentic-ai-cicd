from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if 'ping' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}