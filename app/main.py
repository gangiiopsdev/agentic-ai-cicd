from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return "Invalid host"
    cmd = ["ping", host]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)