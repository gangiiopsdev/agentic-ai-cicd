from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host in allowed_hosts

def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    args = shlex.split(f"ping {host}")
    try:
        subprocess.run(args, check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}