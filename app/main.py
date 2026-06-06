from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host or len(host) > 255:
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', '-c', '1', host], shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)