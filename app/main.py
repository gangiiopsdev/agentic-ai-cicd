from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):