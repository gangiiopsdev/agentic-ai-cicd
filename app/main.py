from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid host")

app = FastAPI()

async def ping(host: str):
    validate_host(host)
    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'result': result.stdout}

@app.get("/ping")
def get_ping(host: str):
    return {'result': await ping(host)}