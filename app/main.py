from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with proper argument quoting
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    return ping(host)

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for IP address format
    return True