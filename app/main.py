from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)
    else:
        return "Invalid host"

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)