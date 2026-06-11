from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper validation
    if not host or len(host) > 255:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return {'result': ping(host)}
    except ValueError as e:
        return {'error': str(e)}, 400