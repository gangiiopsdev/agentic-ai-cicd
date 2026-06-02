from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):  # Input validation missing
    if not validate_host(host):
        raise ValueError("Invalid host")
    return ping(host)
def validate_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts