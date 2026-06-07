from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only certain IP ranges or hostnames.
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "Invalid host", "error": "Host not allowed."}

    # Secure implementation
    command = ['ping'] + shlex.split(host)
    subprocess.call(command)

    return {"status": "completed"}