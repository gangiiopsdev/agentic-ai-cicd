from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}