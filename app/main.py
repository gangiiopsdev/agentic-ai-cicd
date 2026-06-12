from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    if host.strip() and all(c.isalnum() or c in '-.' for c in host):
        subprocess.run(['ping', host], check=True, text=True)
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)