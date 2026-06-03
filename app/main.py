from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isalnum() and len(host) <= 64:
        return subprocess.run(['ping', host], capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str): return safe_ping(host).stdout