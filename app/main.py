from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)