from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)