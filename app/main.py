from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isdigit():
        raise ValueError("Invalid host input")

@app.get("/ping")
async def ping(host: str):,
    validate_host(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}