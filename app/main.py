from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
async def ping_route(host: str):
    return {'result': ping(host)}