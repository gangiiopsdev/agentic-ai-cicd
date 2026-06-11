from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a list of allowed hosts or perform other checks
    return host in ['safehost1', 'safehost2']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Host is not safe")
    subprocess.call(["ping", host])
    return {"status": "completed"}