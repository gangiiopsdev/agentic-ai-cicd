from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return ping(host)

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Basic validation, improve as needed
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    for char in host:
        if char not in valid_chars:
            return False
    return True