from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if not host.isalnum():
        return {'host': host, 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'host': host, 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)