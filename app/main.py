from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if 'ping' in host:
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_endpoint(host: str):      
    return ping(host)