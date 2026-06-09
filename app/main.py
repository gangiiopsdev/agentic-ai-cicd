from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Add your validation logic here (e.g., check if the host is a valid IP address or domain name)
    return True