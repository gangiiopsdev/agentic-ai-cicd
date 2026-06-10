from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):