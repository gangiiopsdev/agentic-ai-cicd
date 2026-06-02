from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run with validation
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'output': result.stdout}
    else:
        raise ValueError('Host not allowed')

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)