from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    return ping(host)

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., check for IP address format
    return True