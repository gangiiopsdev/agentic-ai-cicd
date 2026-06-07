from fastapi import FastAPI
import subprocess
cimport os

def ping(host: str):
    if not host.isnumeric():
        raise ValueError("Invalid host")
    cmd = ["ping", "/bin/sh", "-c", f'echo {host}']
    try:
        output = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}