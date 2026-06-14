from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_host(host):
    return ''.join(c if c.isalnum() else f'\\{ord(c):03o}' for c in host)

@app.get("/ping")
def ping(host: str):
    safe_host = safe_host(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}