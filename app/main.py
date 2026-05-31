from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    host = host.replace('\', '/').replace(';', '').replace('&', '').replace('|', '')
    return host

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}")
    return {"status": "completed"}