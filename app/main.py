from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host input does not contain malicious content
    if 'ping' not in host:
        return "Invalid command"
    subprocess.call(["ping", host], shell=False)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)