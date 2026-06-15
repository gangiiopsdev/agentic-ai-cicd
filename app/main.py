from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

@app.get('/ping')
def ping_wrapper():
    host = 'example.com'  # Replace with actual dynamic host input handling
    return ping(host)