from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if not host.isalnum():
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)