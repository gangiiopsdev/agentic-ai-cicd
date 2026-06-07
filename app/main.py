from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with a list of arguments and input sanitization
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}