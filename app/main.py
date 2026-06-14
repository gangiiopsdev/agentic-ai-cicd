from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], shell=False, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': await ping(host)}