from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    if validate_host(host):
        return ping(host)
    else:
        raise ValueError("Invalid host")

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed characters, IP address format, etc.
    return True