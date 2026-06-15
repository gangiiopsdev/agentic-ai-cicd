from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Fixed implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
async def ping_endpoint(host: str):
    return await ping(host)