from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation of host input
    if not host or ' ' in host:
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}