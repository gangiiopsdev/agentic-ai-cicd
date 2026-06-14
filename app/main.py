from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    return host.replace('.', '').replace('-', '').isalnum()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 400
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}