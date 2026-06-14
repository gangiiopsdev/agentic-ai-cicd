from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric():
        return subprocess.call(['ping', host])
    else:
        return subprocess.call(['ping', '-c', '1', host], stdout=subprocess.DEVNULL)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)