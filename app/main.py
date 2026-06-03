from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.replace('.', '').isnumeric() and len(host.split('.')) == 4

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host address")
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}