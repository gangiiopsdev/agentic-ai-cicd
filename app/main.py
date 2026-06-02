from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    # Simple escaping of special characters
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    host = escape_host(host)
    args = ['ping', host]
    subprocess.call(args, shell=False)

    return {"status": "completed"}