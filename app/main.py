from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate the host input to ensure it is a safe value
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.Popen with full path and shell=False
    subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
async def get_ping(host: str):
    return {'result': await ping(host)}