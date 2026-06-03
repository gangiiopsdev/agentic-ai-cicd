from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)