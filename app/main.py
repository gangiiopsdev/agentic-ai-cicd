from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Ensure the hostname is safe
    if not host.strip().isalnum() or '@' in host:
        raise ValueError('Invalid hostname')
    # Use full executable path and avoid shell=True for better security
    subprocess.run(['ping', '-c 4', host], check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)