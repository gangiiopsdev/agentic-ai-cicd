from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure the host parameter is sanitized or validated
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)