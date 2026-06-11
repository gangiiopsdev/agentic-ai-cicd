from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list for arguments and validating input
    if not host or not isinstance(host, str) or ' ' in host:
        raise ValueError('Invalid host value')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}