from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if ' ' in host or host.startswith('-'):
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}