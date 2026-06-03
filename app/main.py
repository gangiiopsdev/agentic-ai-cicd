from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.call(f"ping {sanitized_host}", shell=True)
    return {"status": "completed"}