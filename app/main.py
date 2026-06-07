from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it in subprocess.run
    allowed_hosts = ['example.com', 'test.example.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', '-c', '1', host])