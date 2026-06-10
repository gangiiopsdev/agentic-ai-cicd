from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with input validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    sanitized_host = ''.join(c for c in host if c.isalnum())  # Sanitize the input
    subprocess.run(['ping', sanitized_host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)