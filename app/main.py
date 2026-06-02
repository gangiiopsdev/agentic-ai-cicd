from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not valid_host(host):
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])

@app.get("/ping")
def ping(host: str):