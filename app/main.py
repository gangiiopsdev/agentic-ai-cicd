from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    # Safer implementation using subprocess.run with args parameter
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return await ping(host)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}