from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_handler(host: str):
    if not is_safe_host(host):
        raise Exception("Invalid host")
    return ping(host)


# Function to validate the host input
def is_safe_host(host: str) -> bool:
    allowed_hosts = ["google.com", "example.com"]  # Replace with actual allowed hosts
    return host in allowed_hosts