from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement validation logic here to ensure 'host' is safe
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}