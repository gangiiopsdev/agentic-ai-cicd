from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host: str) -> bool:
    return host.isalnum() and '.' in host

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid_host"}
    args = ['ping', host]
    subprocess.run(args, shell=False)  # Use subprocess.run instead of subprocess.call
    return {"status": "completed"}