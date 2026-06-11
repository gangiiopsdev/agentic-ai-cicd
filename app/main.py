from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.run instead of subprocess.call with shell=True
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}