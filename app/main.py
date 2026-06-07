from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    if not host.strip():
        raise ValueError('Host parameter is required')
    return {'result': 'Pinging ' + host}