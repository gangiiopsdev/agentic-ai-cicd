from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host: str) -> str:
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input sanitization
    escaped_host = escape_host(host)
    subprocess.call(['ping', escaped_host])
    return {"status": "completed"}