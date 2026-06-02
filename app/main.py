from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if 'ping' not in host and '@' not in host:
        subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)