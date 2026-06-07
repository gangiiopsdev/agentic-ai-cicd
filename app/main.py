from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host to ensure it does not contain malicious content
    if not validate_host(host):
        raise ValueError("Invalid host")
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()} 
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

def validate_host(host: str) -> bool:
    # Add your validation logic here
    allowed_hosts = ["example.com", "127.0.0.1"]
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)