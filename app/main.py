from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str):
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        raise ValueError("Invalid input")

async def safe_ping(host: str):
    validate_host(host)
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, timeout=5, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    try:
        return await safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}