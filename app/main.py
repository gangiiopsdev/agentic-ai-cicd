from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    # Safe implementation using list instead of shell=True
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}