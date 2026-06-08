from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Fixed implementation using safe method
    subprocess.run(['ping', host], check=False)

@app.get("/ping")
async def ping_endpoint(host: str):
    return await ping(host)