from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation
    if not host.isnumeric():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', '-c', '1', host], check=True)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)