from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}