from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host.startswith('192.168.') or host.startswith('10.'):  # Example of basic validation
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_host(host: str):
    return ping(host)