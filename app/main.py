from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement a whitelist of allowed hosts
    return host in ['safehost1', 'safehost2']

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        args = ['ping', host]
        subprocess.call(args)
    else:
        raise ValueError('Host not allowed')

    return {"status": "completed"}