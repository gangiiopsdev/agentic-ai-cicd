from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    # Secure implementation
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}