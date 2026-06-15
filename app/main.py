from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if 'ping' in host or ';' in host:
        raise ValueError('Unsafe input detected')
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}