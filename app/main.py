from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isnumeric():
        return True
    else:
        return False

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    if safe_ping(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "invalid host"}