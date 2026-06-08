from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper quoting
    if host in ['127.0.0.1', 'localhost']:
        subprocess.run(['ping', host], check=True)
    else:
        return {'status': 'rejected'}
    return {'status': 'completed'}