from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., whitelist specific hostnames/IPs
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}