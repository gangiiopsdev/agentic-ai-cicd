from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation to prevent command injection
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}