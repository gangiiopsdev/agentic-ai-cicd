from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' not in host and '.' in host:
        subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)