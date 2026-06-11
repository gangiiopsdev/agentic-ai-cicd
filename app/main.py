from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}