from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Ping failed for {host}: {e}")

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    return ping(host)

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., check for IP address format
    return True