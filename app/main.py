from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e}'

@app.get("/ping")
async def ping_route(host: str):
    return await ping(host)