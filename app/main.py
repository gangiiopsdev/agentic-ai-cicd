from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = shlex.split(f"ping {host}")
        subprocess.run(args, check=True)  # Use subprocess.run instead of subprocess.call for better error handling
        return {'status': 'completed'}
    else:
        return {'status': 'denied', 'message': 'Unauthorized host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)