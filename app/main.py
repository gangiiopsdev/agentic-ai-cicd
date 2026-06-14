from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate user input before using it in subprocess
    if not host.isalnum():
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get="/ping")
def ping_route(host: str):
    return ping(host)