from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if all(c.isalnum() or c in '-.' for c in host):
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping_route(host: str):
    return ping(host)