from fastapi import FastAPI
import subprocess
def validate_input(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):