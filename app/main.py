from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    # Safer implementation
    subprocess.call(['ping', escaped_host])
    return {"status": "completed"}