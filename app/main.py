from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    sanitized_host = host.replace(';', '')  # Basic sanitization to prevent shell injection
    subprocess.run(['ping', sanitized_host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)