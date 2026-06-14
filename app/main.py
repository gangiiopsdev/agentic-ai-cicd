from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.call(f"ping {safe_host}", shell=True)
    return {"status": "completed"}