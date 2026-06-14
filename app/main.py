from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if not all(c.isalnum() or c in '.-_' for c in host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)