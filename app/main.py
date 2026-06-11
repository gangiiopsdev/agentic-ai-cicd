from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host == 'localhost':
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise Exception("Invalid host")

    subprocess.call(["ping", host])

    return {"status": "completed"}