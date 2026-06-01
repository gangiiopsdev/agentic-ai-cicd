from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host format')

@app.get("/ping")
def ping(host: str):

    # Secure implementation
    subprocess.call(['ping', host], shell=False)

    return {"status": "completed"}