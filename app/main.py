from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        run_ping(host)
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}, 400

def validate_host(host: str) -> bool:
    # Add your validation logic here, e.g., regex check for IP addresses or domain names
    return host.isalnum()