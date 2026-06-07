from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement safe host check logic here
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"error": "Invalid host"}
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}