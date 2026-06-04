from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host to prevent injection attacks
    if not all(c.isalnum() or c in '.-:' for c in host):
        raise ValueError("Invalid hostname")
    # Secure implementation using subprocess.run with shell=False
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)