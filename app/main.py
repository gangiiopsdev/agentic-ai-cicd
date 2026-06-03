from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    else:
        raise ValueError("Host not allowed")

allowed_hosts = ["example.com", "test.com"]  # Define a whitelist of allowed hosts