from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.run(["ping", escaped_host], check=True)
    return {"status": "completed"}