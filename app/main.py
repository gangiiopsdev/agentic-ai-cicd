from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the input to ensure it's safe to use with ping
    if not host.isalnum():
        raise ValueError('Invalid host name')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate the input to ensure it's safe to use with ping
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)