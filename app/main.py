from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError('Invalid input')
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str): return safe_ping(host)