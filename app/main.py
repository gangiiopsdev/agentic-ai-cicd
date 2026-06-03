from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)

@app.get("/ping")
def ping_endpoint(host: str):  
    return ping(host)