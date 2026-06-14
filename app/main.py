from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid input"}, 400
    subprocess.call(["ping", host])
    return {"status": "completed"}