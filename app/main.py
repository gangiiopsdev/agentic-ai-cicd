from fastapi import FastAPI
import subprocess
import shlex
import os

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add more allowed hosts as needed
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}

# Preventive controls
- Use a whitelist of allowed hosts.
- Avoid using shell=True in subprocess calls unless absolutely necessary.
- Consider logging and monitoring of subprocess executions for potential misuse.