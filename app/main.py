from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    return hostname.isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "invalid host"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}