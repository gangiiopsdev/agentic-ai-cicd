from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input to prevent injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)