from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with input validation and escaping
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)