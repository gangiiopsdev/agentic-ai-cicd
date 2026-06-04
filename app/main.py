from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Simple validation: allow only alphanumeric characters and some special characters
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)

@app.get="/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid input"}
    command = shlex.split(f'ping {host}')
    subprocess.call(command, shell=False)
    return {"status": "completed"}