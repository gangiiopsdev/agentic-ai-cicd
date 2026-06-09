from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    result = subprocess.call(['ping', host], shell=False)
    return {'status': 'completed' if result == 0 else 'failed'}