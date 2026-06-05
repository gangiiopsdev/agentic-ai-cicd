from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.startswith('192.168.'):
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)