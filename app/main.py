from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.startswith('192.168.'):  # Example of validation, adjust as necessary
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}