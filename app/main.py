from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')
    args = ['ping', safe_host]
    subprocess.call(args)
    return {"status": "completed"}