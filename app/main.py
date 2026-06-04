from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Add appropriate sanitization logic here, e.g., allow only numeric characters and a limited number of periods.
    return host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host.isnumeric():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True)
    return {"status": "completed"}