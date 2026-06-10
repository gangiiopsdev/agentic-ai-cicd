from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with validation
    if '@' in host:
        raise ValueError('Invalid hostname format')
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)