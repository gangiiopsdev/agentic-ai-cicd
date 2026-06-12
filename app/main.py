from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Secure implementation using shlex.quote for command arguments
    sanitized_host = shlex.quote(host)
    subprocess.run(['ping', sanitized_host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)