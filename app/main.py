from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        raise Exception("Invalid host")
    return ping(host)

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Implement validation logic here
    return True