from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.replace('.', '').replace('-', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}