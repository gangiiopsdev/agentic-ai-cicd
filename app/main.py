from fastapi import FastAPI
import subprocess

app = FastAPI()

cimport = subprocess.CalledProcessError

allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
def safe_ping(host: str):
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid host name")
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}

@app.get="/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return response
    except cimport as e:
        return {"status": "failed", "error": e.stderr}