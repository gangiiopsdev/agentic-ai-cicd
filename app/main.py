from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with explicit arguments and shell=False
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    return ping(host)

def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed IP addresses or domain names
    return True