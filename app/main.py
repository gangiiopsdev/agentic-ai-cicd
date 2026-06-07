from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_hostname(hostname):
    return hostname.strip() != '.' and not hostname.startswith('-')

@app.get("/ping")
def ping(host: str):
    if not is_valid_hostname(host):
        raise ValueError("Invalid hostname")
    command = shlex.split(f"ping {host}")
    subprocess.run(command, check=True)
    return {"status": "completed"}