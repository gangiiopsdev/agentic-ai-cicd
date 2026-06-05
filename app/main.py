from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):