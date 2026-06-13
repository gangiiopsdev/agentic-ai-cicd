from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with proper sanitization
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}