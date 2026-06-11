from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with args instead of shell=True
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}