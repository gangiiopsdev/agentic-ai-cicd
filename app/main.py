from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add allowed hosts here
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)  # Use subprocess.run for better control and error handling
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 403