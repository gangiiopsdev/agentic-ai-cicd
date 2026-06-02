from fastapi import FastAPI
import subprocess
def validate_host(host):
    if any(char in host for char in [';', '|', '&', '<', '>', '$']):
        raise ValueError('Invalid host input')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], check=True)  # Use subprocess.run to handle return code
    return {"status": "completed"}