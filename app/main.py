from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum():
        raise ValueError("Invalid input")
    return host

@app.get("/ping")
def ping(host: str):
    valid_host = validate_host(host)
    args = ['ping', f'-c 1 {valid_host}']
    subprocess.run(args, check=True)
    return {"status": "completed"}